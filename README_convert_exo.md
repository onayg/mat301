# Script de Conversion des Exercices LaTeX

Ce script convertit automatiquement tous les exercices LaTeX du format `\noindent\textbf{Exercice X.}` vers l'environnement `exo`.

## Utilisation

```bash
python3 convert_to_exo.py
```

## Fonctionnalités

### 1. Ajout automatique de l'environnement exo
Le script ajoute automatiquement la définition de l'environnement `exo` dans chaque fichier :

```latex
% Définition de l'environnement exo
\newcounter{exo}
\newenvironment{exo}{%
  \refstepcounter{exo}%
  \vspace{1em}%
  \noindent\textbf{Exercice \theexo.}%
  \par\noindent
}{%
  \vspace{1em}%
}
```

### 2. Conversion automatique des exercices

**Avant :**
```latex
\noindent\textbf{Exercice 1.}

Soit $(E, d)$ un espace métrique...

\vspace{1em}

\noindent\textbf{Exercice 2.}

Montrer que...
```

**Après :**
```latex
\begin{exo}
Soit $(E, d)$ un espace métrique...
\end{exo}

\begin{exo}
Montrer que...
\end{exo}
```

### 3. Gestion robuste

- **Sauvegarde automatique** : Crée des fichiers `.tex.bak` avant modification
- **Restauration automatique** : Si des backups existent, ils sont restaurés avant la conversion
- **Détection intelligente** : Gère les exercices avec annotations (ex: `Exercice 1. (Distance SNCF)`)
- **Nettoyage** : Supprime automatiquement les `\vspace{1em}` redondants

### 4. Statistiques

Le script affiche :
- Le nombre de fichiers trouvés
- Le nombre d'exercices détectés par fichier
- Le nombre de fichiers modifiés
- Les erreurs éventuelles

## Exemple de sortie

```
============================================================
Script de conversion des exercices vers l'environnement exo
============================================================

📁 Dossier source: /home/gonenc/projects/mat301/tds/source
✓ 4 fichier(s) .tex trouvé(s)

📄 Traitement de td1.tex...
  ✓ Environnement exo ajouté
  ✓ 6 exercice(s) détecté(s)
  ✓ Sauvegarde créée: td1.tex.bak
  ✅ 6 exercice(s) converti(s)

============================================================
✅ Traitement terminé: 3/4 fichier(s) modifié(s)
============================================================
```

## Utilisation de l'environnement exo

Une fois la conversion effectuée, vous pouvez utiliser l'environnement `exo` dans vos nouveaux documents :

```latex
\begin{exo}
Votre énoncé d'exercice ici...
\end{exo}
```

Les exercices seront automatiquement numérotés (1, 2, 3, etc.).

## Fichiers traités

Le script traite tous les fichiers `.tex` dans le dossier `tds/source/` :
- `td1.tex`
- `td2.tex`
- `td3.tex`
- `quiz-revision.tex`

## Sécurité

- Les fichiers originaux sont sauvegardés avec l'extension `.tex.bak`
- Pour restaurer un fichier, copiez simplement le `.bak` :
  ```bash
  cp tds/source/td1.tex.bak tds/source/td1.tex
  ```
