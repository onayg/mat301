#!/usr/bin/env python3
"""
Script robuste pour convertir les exercices LaTeX vers l'environnement exo.
Traite tous les fichiers .tex dans le dossier tds/source.
"""

import re
import os
from pathlib import Path


def has_exo_environment(content: str) -> bool:
    """Vérifie si l'environnement exo est déjà défini dans le contenu."""
    return r'\newenvironment{exo}' in content


def add_exo_environment(content: str) -> str:
    """Ajoute la définition de l'environnement exo après les packages."""
    if has_exo_environment(content):
        print("  ✓ Environnement exo déjà présent")
        return content

    exo_definition = """
% Définition de l'environnement exo
\\newcounter{exo}
\\newenvironment{exo}{%
  \\refstepcounter{exo}%
  \\vspace{1em}%
  \\noindent\\textbf{Exercice \\theexo.}%
  \\par\\noindent
}{%
  \\vspace{1em}%
}
"""

    # Chercher la ligne \title
    title_pattern = r'(\\title\{)'

    if re.search(title_pattern, content):
        content = re.sub(title_pattern, lambda m: exo_definition + '\n' + m.group(0), content)
        print("  ✓ Environnement exo ajouté")
    else:
        print("  ⚠ Impossible de trouver \\title, environnement non ajouté")

    return content


def convert_exercises_to_exo(content: str) -> tuple:
    """
    Convertit tous les exercices en environnements exo.
    Retourne le contenu modifié et le nombre d'exercices convertis.
    """
    # Pattern pour détecter un exercice
    # Capture: \vspace optionnel + \noindent\textbf{Exercice X.} + texte optionnel entre parenthèses
    exercise_pattern = r'(?:^\\vspace\{[^}]+\}\s*\n+)?^\\noindent\\textbf\{Exercice\s+\d+\.\}(?:\s*\([^)]+\))?'

    # Trouver tous les exercices
    matches = list(re.finditer(exercise_pattern, content, re.MULTILINE))

    if not matches:
        print("  ℹ Aucun exercice trouvé")
        return content, 0

    print(f"  ✓ {len(matches)} exercice(s) détecté(s)")

    # Découper le contenu en sections
    sections = []
    last_end = 0

    for i, match in enumerate(matches):
        # Ajouter le contenu avant cet exercice
        if match.start() > last_end:
            sections.append(content[last_end:match.start()])

        # Déterminer la fin de cet exercice
        if i < len(matches) - 1:
            # Il y a un exercice suivant
            exercise_content = content[match.end():matches[i+1].start()]
        else:
            # C'est le dernier exercice
            # Chercher \end{document}
            end_doc_pos = content.find(r'\end{document}', match.end())
            if end_doc_pos != -1:
                exercise_content = content[match.end():end_doc_pos]
            else:
                exercise_content = content[match.end():]

        # Nettoyer le contenu de l'exercice
        exercise_content = exercise_content.strip()

        # Enlever les \vspace{1em} à la fin s'il y en a
        exercise_content = re.sub(r'\n*\\vspace\{[^}]+\}\s*$', '', exercise_content)

        # Créer le nouvel environnement exo
        new_exercise = f"\\begin{{exo}}\n{exercise_content}\n\\end{{exo}}\n\n"
        sections.append(new_exercise)

        last_end = matches[i+1].start() if i < len(matches) - 1 else (
            content.find(r'\end{document}', match.end()) if content.find(r'\end{document}', match.end()) != -1 else len(content)
        )

    # Ajouter le reste du document (généralement \end{document})
    if last_end < len(content):
        sections.append(content[last_end:])

    new_content = ''.join(sections)
    return new_content, len(matches)


def process_tex_file(filepath: Path) -> bool:
    """
    Traite un fichier .tex pour convertir les exercices.
    Retourne True si le fichier a été modifié.
    """
    print(f"\n📄 Traitement de {filepath.name}...")

    # Lire le contenu
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            original_content = f.read()
    except Exception as e:
        print(f"  ❌ Erreur de lecture: {e}")
        return False

    # Ajouter l'environnement exo si nécessaire
    content = add_exo_environment(original_content)

    # Convertir les exercices
    content, num_converted = convert_exercises_to_exo(content)

    # Vérifier si le contenu a changé
    if content == original_content:
        print("  ℹ Aucune modification nécessaire")
        return False

    # Créer une sauvegarde
    backup_path = filepath.with_suffix('.tex.bak')
    try:
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(original_content)
        print(f"  ✓ Sauvegarde créée: {backup_path.name}")
    except Exception as e:
        print(f"  ⚠ Impossible de créer la sauvegarde: {e}")

    # Écrire le nouveau contenu
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ {num_converted} exercice(s) converti(s)")
        return True
    except Exception as e:
        print(f"  ❌ Erreur d'écriture: {e}")
        return False


def restore_backups(source_dir: Path):
    """Restaure les fichiers depuis les backups."""
    backups = list(source_dir.glob('*.tex.bak'))
    for backup in backups:
        original = backup.with_suffix('')
        if original.exists():
            with open(backup, 'r', encoding='utf-8') as f:
                content = f.read()
            with open(original, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Restauré: {original.name}")


def main():
    """Point d'entrée principal du script."""
    print("=" * 60)
    print("Script de conversion des exercices vers l'environnement exo")
    print("=" * 60)

    # Trouver le dossier tds/source
    script_dir = Path(__file__).parent
    source_dir = script_dir / 'tds' / 'source'

    if not source_dir.exists():
        print(f"❌ Dossier {source_dir} introuvable")
        return

    print(f"\n📁 Dossier source: {source_dir}")

    # Restaurer d'abord les backups s'ils existent
    backups = list(source_dir.glob('*.tex.bak'))
    if backups:
        print(f"\n⚠ {len(backups)} backup(s) trouvé(s), restauration...")
        restore_backups(source_dir)

    # Trouver tous les fichiers .tex (excluant les .bak)
    tex_files = sorted([f for f in source_dir.glob('*.tex')
                       if not f.name.endswith('.bak')])

    if not tex_files:
        print("❌ Aucun fichier .tex trouvé")
        return

    print(f"✓ {len(tex_files)} fichier(s) .tex trouvé(s)")

    # Traiter chaque fichier
    modified_count = 0
    for tex_file in tex_files:
        if process_tex_file(tex_file):
            modified_count += 1

    # Résumé
    print("\n" + "=" * 60)
    print(f"✅ Traitement terminé: {modified_count}/{len(tex_files)} fichier(s) modifié(s)")
    print("=" * 60)


if __name__ == '__main__':
    main()
