# Résumé du cours : Topologie Metrique

Ce document propose une balade à travers les concepts fondamentaux des espaces métriques, en s'inspirant du cours, des feuilles de TD, et du polycopié de référence. 
### 1. La Notion de Distance

Au cœur de l'analyse se trouve l'idée de "proximité". Un **espace métrique** est la formalisation la plus simple de cette idée. C'est un couple $(E, d)$ où $E$ est un ensemble et $d: E \times E \to \mathbb{R}_{\geq 0}$ est une **distance** (ou métrique), qui doit satisfaire pour tous $x, y, z \in E$:
1.  **Séparation :** $d(x,y) = 0 \iff x=y$.
2.  **Symétrie :** $d(x,y) = d(y,x)$.
3.  **Inégalité triangulaire :** $d(x,z) \leq d(x,y) + d(y,z)$.

Cette dernière propriété, l'inégalité triangulaire, est cruciale ; elle capture l'intuition que le chemin direct est toujours le plus court.

**Exercice :** Montrer que $\vert d(x,z)-d(x,y) \vert \leq d(y,z)$ pour tout $x,y,z \in E$.

**Quelques exemples fondamentaux :**

*   **La distance usuelle sur $\mathbb{R}$** est simplement $d(x,y) = |x-y|$.
*   **Sur $\mathbb{R}^n$**, plusieurs distances coexistent. Pour $x=(x_i), y=(y_i)$:
    *   $d_1(x,y) = \sum_{i=1}^n |x_i - y_i|$ (la distance "Manhattan").
    *   $d_2(x,y) = \sqrt{\sum_{i=1}^n |x_i - y_i|^2}$ (la distance euclidienne).
    *   $d_\infty(x,y) = \max_{i=1..n} |x_i - y_i|$ (la distance "sup").
    Comme nous le verrons, bien que numériquement différentes, ces distances décrivent la même notion de "proximité" sur $\mathbf{R}^n$ (cf. TD2, elles sont topologiquement équivalentes).
*   **Sur l'espace $\mathcal{C}([0,1], \mathbb{R})$** des fonctions continues sur $[0,1]$, la **distance de la convergence uniforme** est $d_\infty(f,g) = \sup_{t \in [0,1]} |f(t)-g(t)|$.
*   **La distance discrète** sur n'importe quel ensemble $E$ : $d(x,y) = 1$ si $x \neq y$ et $0$ sinon. C'est un cas extrême où tous les points sont "isolés" les uns des autres.
*   **La distance SNCF (TD1)** sur $\mathbb{R}^2$ est un exemple plus exotique où la distance entre deux points dépend de leur position par rapport à l'origine (Paris !), illustrant que les métriques peuvent être non-triviales.

**Espaces ultramétriques :** Une **ultramétrique** sur un ensemble $E$ est une distance $d : E \times E \to \mathbb{R}_{\geq 0}$ satisfaisant une inégalité triangulaire renforcée :
$$ d(x,z) \leq \max\{d(x,y), d(y,z)\} \quad \text{pour tous } x, y, z \in E. $$
Cette condition est plus forte que l'inégalité triangulaire usuelle (puisque $\max\{a,b\} \leq a+b$), et elle confère aux espaces ultramétriques des propriétés surprenantes. Par exemple, dans un espace ultramétrique, tout point d'une boule ouverte en est un centre (TD3, Exercice 4a), et toute boule ouverte est également fermée (TD3, Exercice 4c) !

L'exemple fondamental est la **distance $p$-adique** sur $\mathbb{Q}$ (TD3, Exercice 4). Pour un nombre premier $p$ fixé, on définit d'abord la valuation $p$-adique $v_p : \mathbb{Q} \to \mathbb{Z} \cup \{+\infty\}$ (le plus grand exposant de $p$ dans la décomposition en facteurs premiers), puis la norme $p$-adique $|x|_p = p^{-v_p(x)}$ pour $x \neq 0$ et $|0|_p = 0$. La distance $p$-adique est alors $d_p(x,y) = |x-y|_p$. Cette distance capture une notion de "proximité" radicalement différente de la distance usuelle : deux nombres sont $p$-adiquement proches s'ils ont beaucoup de facteurs $p$ en commun dans leur différence.

**Constructions de nouvelles métriques :**

Les métriques peuvent être construites de multiples façons. Voici les constructions fondamentales qui permettent d'engendrer de nouveaux espaces métriques à partir de structures existantes.

**Distance induite par une norme :** Soit $\mathbb{K}$ le corps des réels $\mathbb{R}$ ou des complexes $\mathbb{C}$. Un **espace vectoriel normé** sur $\mathbb{K}$ est un couple $(E, || \cdot||)$ où $E$ est un $\mathbb{K}$-espace vectoriel et $|| \cdot|| : E \to \mathbb{R}_{\geq 0}$ est une **norme**, c'est-à-dire une application satisfaisant pour tous $x, y \in E$ et tout scalaire $\lambda \in \mathbb{K}$ :
1. **Séparation :** $||x|| = 0 \iff x = 0$ ;
2. **Homogénéité :** $||\lambda x|| = |\lambda| \cdot ||x||$ ;
3. **Inégalité triangulaire :** $||x + y|| \leq ||x|| + ||y||$.

Tout espace vectoriel normé devient naturellement un espace métrique avec la **distance induite** $d(x,y) = ||x-y||$. Cette distance hérite de la structure vectorielle : elle est invariante par translation, $d(x+a, y+a) = d(x,y)$ pour tout $a \in E$ (cf. TD2). 

**Distance induite sur un sous-ensemble :** Si $(E, d)$ est un espace métrique et $A \subseteq E$, on peut munir $A$ de la **distance induite** (ou restriction) $d|_A : A \times A \to \mathbb{R}_{\geq 0}$ définie par $d|_A(x,y) = d(x,y)$ pour $x, y \in A$. 

**Distance pushforward (ou image directe) :** Plus généralement, si $f : A \to E$ est une application **injective** d'un ensemble $A$ vers un espace métrique $(E, d)$, on peut munir $A$ d'une distance définie par :
$$ d_f(a, a') := d(f(a), f(a')). $$
Cette distance sur $A$ est appelée la **distance pushforward** ou **distance image**. Elle "tire en arrière" la métrique de $E$ via $f$. L'injectivité de $f$ garantit la propriété de séparation : $d_f(a, a') = 0 \iff f(a) = f(a') \iff a = a'$. Cette construction permet de transférer la structure métrique de l'espace d'arrivée vers l'ensemble de départ. La distance induite $d_A$ ci-dessous n'est qu'un example de la distance image, quand $A$ est un sous-ensemble de $E$, en prenant $f$ l'injection canonique $(x\mapsto x).$

**Distance produit :** Lorsqu'on a deux espaces métriques $(E, d)$ et $(F, \delta)$, on peut construire un espace métrique sur le produit cartésien $E \times F$. Une distance naturelle est la **distance produit** (ou distance sup) définie par :
$$ d_\infty((x_1, y_1), (x_2, y_2)) = \max\{d(x_1, x_2), \delta(y_1, y_2)\}. $$
Cette construction est fondamentale. Elle permet de comprendre la convergence dans le produit : une suite $(u_n, v_n)$ converge vers $(u, v)$ dans $(E \times F, d_\infty)$ si et seulement si $u_n \to u$ dans $(E, d)$ et $v_n \to v$ dans $(F, \delta)$ (cf. TD4, Exercice 5). On peut aussi considérer d'autres distances produit, comme $d_1((x_1, y_1), (x_2, y_2)) = d(x_1, x_2) + \delta(y_1, y_2)$ ou la distance euclidienne $d_2((x_1, y_1), (x_2, y_2)) = \sqrt{d(x_1, x_2)^2 + \delta(y_1, y_2)^2}$, qui sont topologiquement équivalentes.

### 2. Topologie : Ouverts, Fermés, et Voisinage

La distance nous permet de définir les **boules ouvertes** $B(x,r) = \{y \in E \mid d(x,y) < r\}$ et les **boules fermées** $B_{\mathtt{F}}(x,r) = \{y \in E \mid d(x,y) \leq r\}$. Avec notre notation, $r$ peut être nul, auquel cas $B(x,0) = \emptyset$ et $B_{\mathtt{F}}(x,0) = \{x\}$.

**Voisinages :** Une partie $V \subseteq E$ est un **voisinage** d'un point $x \in E$ s'il existe un rayon $r > 0$ tel que la boule ouverte $B(x,r)$ soit entièrement contenue dans $V$. Autrement dit, $V$ est un voisinage de $x$ si et seulement si $x$ appartient à l'intérieur de $V$ (l'intérieur sera défini ci-dessous). On note $\mathcal{V}(x)$ (ou $\mathcal{V}_d(x)$ quand on veut préciser la métrique) l'ensemble de tous les voisinages de $x$. Les voisinages capturent l'idée de "proximité locale" autour d'un point : un voisinage est une région qui contient $x$ avec "un peu d'espace de manœuvre" autour de lui. Remarquons qu'un voisinage n'est pas nécessairement ouvert ; par exemple, $[0, 1]$ est un voisinage de $1/2$ dans $\mathbb{R}$, bien qu'il ne soit pas ouvert.

Une partie $U \subseteq E$ est dite **ouverte** si chaque point de $U$ est le centre d'une petite boule ouverte non-vide entièrement contenue dans $U$. Formellement, $\forall x \in U, \exists r>0$ tel que $B(x,r) \subseteq U$. Les caractérisations suivantes sont équivalentes :
- $U$ est ouvert ;
- $U$ est un voisinage de chacun de ses points ;
- $U = \mathring{U}$ (l'intérieur de $U$ est $U$ tout entier ; l'intérieur sera défini ci-dessous comme le plus grand ouvert contenu dans $U$) ;
- $E \setminus U$ est fermé.

Les boules ouvertes sont elles-mêmes des ouverts (Montrer le!). L'union quelconque et l'intersection finie d'ouverts sont des ouverts.

Un ensemble $F$ est **fermé** si son complémentaire $E \setminus F$ est ouvert. Les caractérisations suivantes sont équivalentes :
- $F$ est fermé ;
- $F = \bar{F}$ (l'adhérence de $F$ est $F$ tout entier ; l'adhérence sera définie ci-dessous comme le plus petit fermé contenant $F$) ;
- Toute suite convergente d'éléments de $F$ a sa limite dans $F$ (la convergence est définie en §3) ;


L'intersection quelconque et l'union finie de fermés sont des fermés. Le cercle unité $S^1$ dans $\mathbb{R}^2$ est un exemple de fermé (TD3).

Attention, "ouvert" et "fermé" ne sont pas des contraires. Une partie peut être les deux (dans l'espace discret, toutes les parties le sont) ou aucun des deux (comme $[0,1[$ dans $\mathbb{R}$). Dans un espace ultramétrique, on peut montrer que les boules ouvertes sont aussi fermées (TD3) !

**Les opérateurs topologiques :** Pour toute partie $A \subseteq E$, on peut définir trois régions fondamentales qui décomposent l'espace :

L'**intérieur** de $A$, noté $\mathring{A}$, est le plus grand ouvert contenu dans $A$. On peut le caractériser de manière équivalente comme l'ensemble des points dont $A$ est un voisinage :
$$\mathring{A} = \{x \in A \mid A \in \mathcal{V}(x)\} = \{x \in E \mid \exists r > 0, B(x,r) \subseteq A\}.$$

L'**adhérence** de $A$, notée $\bar{A}$, est le plus petit fermé contenant $A$. C'est l'ensemble des points "infiniment proches" de $A$, au sens où toute boule centrée en eux rencontre $A$ :
$$\bar{A} = \{x \in E \mid \forall r>0, B(x,r) \cap A \neq \emptyset\}.$$

L'**extérieur** de $A$, noté $\text{ext}(A)$, est l'intérieur du complémentaire : $\text{ext}(A) = \mathring{E \setminus A}$. C'est l'ensemble des points qui sont "loin" de $A$, au sens où ils possèdent un voisinage entièrement disjoint de $A$.

La **frontière** de $A$, notée $\text{Fr}(A)$, est définie par $\text{Fr}(A) = \bar{A} \setminus \mathring{A}$. C'est l'ensemble des points qui sont à la fois infiniment proches de $A$ et de son complémentaire : ni intérieurs à $A$, ni extérieurs à $A$. Ces trois ensembles forment une partition de l'espace tout entier :
$$E = \mathring{A} \sqcup \text{Fr}(A) \sqcup \text{ext}(A).$$

L'exercice du TD3 demandant si $\overline{B(a,r)} = B_{\mathtt{F}}(a,r)$ est instructif. La réponse est non en général. Dans un espace discret, $\overline{B(x,1)} = \overline{\{x\}} = \{x\}$, mais $B_{\mathtt{F}}(x,1) = E$.

**Équivalence topologique de métriques :** Deux distances $d_1$ et $d_2$ sur un même ensemble $E$ sont dites **topologiquement équivalentes** si elles définissent la même famille d'ouverts. Cette notion est fondamentale car elle nous dit quand deux métriques décrivent "la même géométrie" du point de vue topologique.

**Proposition (caractérisation par les voisinages) :** Deux distances $d_1$ et $d_2$ sur $E$ sont topologiquement équivalentes si et seulement si pour tout point $x \in E$, les systèmes de voisinages coïncident : $\mathcal{V}_{d_1}(x) = \mathcal{V}_{d_2}(x)$.

En pratique, pour montrer que deux distances sont topologiquement équivalentes, on utilise souvent le critère suivant : pour tout $x \in E$ et tout $\varepsilon > 0$, il existe $\eta, \eta' > 0$ tels que
$$ B_{d_2}(x, \eta) \subseteq B_{d_1}(x, \varepsilon) \quad \text{et} \quad B_{d_1}(x, \eta') \subseteq B_{d_2}(x, \varepsilon). $$
Cela signifie que toute boule pour une distance contient une boule pour l'autre distance, et vice-versa (cf. TD2, Exercice 3).

**Exemple fondamental :** Sur $\mathbb{R}^n$, les distances $d_1$, $d_2$, et $d_\infty$ sont topologiquement équivalentes. On peut le montrer en vérifiant que pour tout $x \in \mathbb{R}^n$, on a $\mathcal{V}_{d_1}(x) = \mathcal{V}_{d_2}(x) = \mathcal{V}_{d_\infty}(x)$. Par exemple, le TD2 (Exercice 4) démontre explicitement que $\mathcal{V}_{d_1}(0) = \mathcal{V}_{d_\infty}(0)$ sur $\mathbb{R}^2$, et par invariance par translation (ces distances proviennent de normes), cela s'étend à tout point de $\mathbb{R}^n$. Cette équivalence a des conséquences profondes : une suite converge pour l'une de ces distances si et seulement si elle converge pour les autres, et la limite est la même (cf. TD4, Exercice 4). Autrement dit, sur $\mathbb{R}^n$, la convergence coordonnée par coordonnée (pour $d_1$ ou $d_\infty$) équivaut à la convergence euclidienne (pour $d_2$).

### 3. Suites : Points d'Accumulation et Convergence

Les suites sont l'outil dynamique pour explorer la topologie d'un espace. Une suite est une fonction $u: \mathbb{N} \to E$.

Un point $a \in E$ est un **point d'accumulation** de la suite $(u_n)$ si la suite "revient" infiniment souvent aussi près que l'on veut de $a$. Formellement :
$$ \forall \varepsilon > 0, \forall N \in \mathbb{N}, \exists n \geq N \text{ tel que } d(u_n, a) < \varepsilon. $$
Cette définition est équivalente à la caractérisation ensembliste suivante :

**Proposition :** $a$ est un point d'accumulation de $(u_n)$ si et seulement si pour tout $\varepsilon > 0$, l'ensemble des indices $\{ n \in \mathbb{N} \mid u_n \in B(a, \varepsilon) \}$ est infini.

La **convergence** est un concept plus fort. Une suite $(u_n)$ converge vers une limite $\ell \in E$ si, à partir d'un certain rang, tous les termes restent aussi proches que l'on veut de $\ell$ :
$$ \forall \varepsilon > 0, \exists N \in \mathbb{N}, \forall n \geq N, d(u_n, \ell) < \varepsilon. $$
Si une suite converge vers $\ell$, alors $\ell$ est son *unique* point d'accumulation. Toute sous-suite convergera aussi vers $\ell$. L'inverse n'est pas vrai : la suite $u_n = 1/n$ si $n$ est impaire $n$ sinon, dans $\mathbb{R}$ a deux points d'accumulation ne converge pas mais poss\`ede un seul point d'accumulation.

**Proposition (caractérisation ensembliste) :** $(u_n)$ converge vers $\ell$ si et seulement si pour tout $\varepsilon > 0$, l'ensemble des indices $\{ n \in \mathbb{N} \mid u_n \notin B(\ell, \varepsilon) \}$ est fini. Autrement dit, l'image réciproque de toute boule centrée en $\ell$ est une partie **cofinie** de $\mathbb{N}$ (son complémentaire est fini).

Le lien entre suites et topologie est intime :
*   **Caractérisation séquentielle de l'adhérence :** $x \in \bar{A}$ si et seulement si il existe une suite $(a_n)$ d'éléments de $A$ qui converge vers $x$.
*   **Caractérisation séquentielle des fermés :** Une partie $F$ est fermée si et seulement si les limites de toutes les suites convergentes d'éléments de $F$ appartiennent à $F$.

# Résumé du cours : Topologie Metrique

Ce document propose une balade à travers les concepts fondamentaux des espaces métriques, en s'inspirant du cours, des feuilles de TD, et du polycopié de référence. 
### 1. La Notion de Distance

Au cœur de l'analyse se trouve l'idée de "proximité". Un **espace métrique** est la formalisation la plus simple de cette idée. C'est un couple $(E, d)$ où $E$ est un ensemble et $d: E \times E \to \mathbb{R}_{\geq 0}$ est une **distance** (ou métrique), qui doit satisfaire pour tous $x, y, z \in E$:
1.  **Séparation :** $d(x,y) = 0 \iff x=y$.
2.  **Symétrie :** $d(x,y) = d(y,x)$.
3.  **Inégalité triangulaire :** $d(x,z) \leq d(x,y) + d(y,z)$.

Cette dernière propriété, l'inégalité triangulaire, est cruciale ; elle capture l'intuition que le chemin direct est toujours le plus court.

**Exercice :** Montrer que $\vert d(x,z)-d(x,y) \vert \leq d(y,z)$ pour tout $x,y,z \in E$.

**Quelques exemples fondamentaux :**

*   **La distance usuelle sur $\mathbb{R}$** est simplement $d(x,y) = |x-y|$.
*   **Sur $\mathbb{R}^n$**, plusieurs distances coexistent. Pour $x=(x_i), y=(y_i)$:
    *   $d_1(x,y) = \sum_{i=1}^n |x_i - y_i|$ (la distance "Manhattan").
    *   $d_2(x,y) = \sqrt{\sum_{i=1}^n |x_i - y_i|^2}$ (la distance euclidienne).
    *   $d_\infty(x,y) = \max_{i=1..n} |x_i - y_i|$ (la distance "sup").
    Comme nous le verrons, bien que numériquement différentes, ces distances décrivent la même notion de "proximité" sur $\mathbf{R}^n$ (cf. TD2, elles sont topologiquement équivalentes).
*   **Sur l'espace $\mathcal{C}([0,1], \mathbb{R})$** des fonctions continues sur $[0,1]$, la **distance de la convergence uniforme** est $d_\infty(f,g) = \sup_{t \in [0,1]} |f(t)-g(t)|$.
*   **La distance discrète** sur n'importe quel ensemble $E$ : $d(x,y) = 1$ si $x \neq y$ et $0$ sinon. C'est un cas extrême où tous les points sont "isolés" les uns des autres.
*   **La distance SNCF (TD1)** sur $\mathbb{R}^2$ est un exemple plus exotique où la distance entre deux points dépend de leur position par rapport à l'origine (Paris !), illustrant que les métriques peuvent être non-triviales.

**Espaces ultramétriques :** Une **ultramétrique** sur un ensemble $E$ est une distance $d : E \times E \to \mathbb{R}_{\geq 0}$ satisfaisant une inégalité triangulaire renforcée :
$$ d(x,z) \leq \max\{d(x,y), d(y,z)\} \quad \text{pour tous } x, y, z \in E. $$
Cette condition est plus forte que l'inégalité triangulaire usuelle (puisque $\max\{a,b\} \leq a+b$), et elle confère aux espaces ultramétriques des propriétés surprenantes. Par exemple, dans un espace ultramétrique, tout point d'une boule ouverte en est un centre (TD3, Exercice 4a), et toute boule ouverte est également fermée (TD3, Exercice 4c) !

L'exemple fondamental est la **distance $p$-adique** sur $\mathbb{Q}$ (TD3, Exercice 4). Pour un nombre premier $p$ fixé, on définit d'abord la valuation $p$-adique $v_p : \mathbb{Q} \to \mathbb{Z} \cup \{+\infty\}$ (le plus grand exposant de $p$ dans la décomposition en facteurs premiers), puis la norme $p$-adique $|x|_p = p^{-v_p(x)}$ pour $x \neq 0$ et $|0|_p = 0$. La distance $p$-adique est alors $d_p(x,y) = |x-y|_p$. Cette distance capture une notion de "proximité" radicalement différente de la distance usuelle : deux nombres sont $p$-adiquement proches s'ils ont beaucoup de facteurs $p$ en commun dans leur différence.

**Constructions de nouvelles métriques :**

Les métriques peuvent être construites de multiples façons. Voici les constructions fondamentales qui permettent d'engendrer de nouveaux espaces métriques à partir de structures existantes.

**Distance induite par une norme :** Soit $\mathbb{K}$ le corps des réels $\mathbb{R}$ ou des complexes $\mathbb{C}$. Un **espace vectoriel normé** sur $\mathbb{K}$ est un couple $(E, || \cdot||)$ où $E$ est un $\mathbb{K}$-espace vectoriel et $|| \cdot|| : E \to \mathbb{R}_{\geq 0}$ est une **norme**, c'est-à-dire une application satisfaisant pour tous $x, y \in E$ et tout scalaire $\lambda \in \mathbb{K}$ :
1. **Séparation :** $||x|| = 0 \iff x = 0$ ;
2. **Homogénéité :** $||\lambda x|| = |\lambda| \cdot ||x||$ ;
3. **Inégalité triangulaire :** $||x + y|| \leq ||x|| + ||y||$.

Tout espace vectoriel normé devient naturellement un espace métrique avec la **distance induite** $d(x,y) = ||x-y||$. Cette distance hérite de la structure vectorielle : elle est invariante par translation, $d(x+a, y+a) = d(x,y)$ pour tout $a \in E$ (cf. TD2). 

**Distance induite sur un sous-ensemble :** Si $(E, d)$ est un espace métrique et $A \subseteq E$, on peut munir $A$ de la **distance induite** (ou restriction) $d|_A : A \times A \to \mathbb{R}_{\geq 0}$ définie par $d|_A(x,y) = d(x,y)$ pour $x, y \in A$. Les ouverts de $(A, d|_A)$ (voir §2 pour les définitions) sont exactement les ensembles de la forme $U \cap A$ où $U$ est ouvert dans $(E, d)$ — autrement dit, un ensemble est ouvert dans $A$ s'il est la trace d'un ouvert de $E$. De même, les fermés de $(A, d|_A)$ sont les ensembles de la forme $F \cap A$ où $F$ est fermé dans $(E, d)$.

**Distance pushforward (ou image directe) :** Plus généralement, si $f : A \to E$ est une application **injective** d'un ensemble $A$ vers un espace métrique $(E, d)$, on peut munir $A$ d'une distance définie par :
$$ d_f(a, a') := d(f(a), f(a')). $$
Cette distance sur $A$ est appelée la **distance pushforward** ou **distance image**. Elle "tire en arrière" la métrique de $E$ via $f$. L'injectivité de $f$ garantit la propriété de séparation : $d_f(a, a') = 0 \iff f(a) = f(a') \iff a = a'$. Cette construction permet de transférer la structure métrique de l'espace d'arrivée vers l'ensemble de départ. La distance induite $d_A$ ci-dessous n'est qu'un example de la distance image, quand $A$ est un sous-ensemble de $E$, en prenant $f$ l'injection canonique $(x\mapsto x).$

**Distance produit :** Lorsqu'on a deux espaces métriques $(E, d)$ et $(F, \delta)$, on peut construire un espace métrique sur le produit cartésien $E \times F$. Une distance naturelle est la **distance produit** (ou distance sup) définie par :
$$ d_\infty((x_1, y_1), (x_2, y_2)) = \max\{d(x_1, x_2), \delta(y_1, y_2)\}. $$
Cette construction est fondamentale. Elle permet de comprendre la convergence dans le produit : une suite $(u_n, v_n)$ converge vers $(u, v)$ dans $(E \times F, d_\infty)$ si et seulement si $u_n \to u$ dans $(E, d)$ et $v_n \to v$ dans $(F, \delta)$ (cf. TD4, Exercice 5). On peut aussi considérer d'autres distances produit, comme $d_1((x_1, y_1), (x_2, y_2)) = d(x_1, x_2) + \delta(y_1, y_2)$ ou la distance euclidienne $d_2((x_1, y_1), (x_2, y_2)) = \sqrt{d(x_1, x_2)^2 + \delta(y_1, y_2)^2}$, qui sont topologiquement équivalentes.

### 2. Vocabulaire Topologique : Ouverts, Fermés, et Voisinage

La distance nous permet de définir les **boules ouvertes** $B(x,r) = \{y \in E \mid d(x,y) < r\}$ et les **boules fermées** $B_{\mathtt{F}}(x,r) = \{y \in E \mid d(x,y) \leq r\}$. Avec notre notation, $r$ peut être nul, auquel cas $B(x,0) = \emptyset$ et $B_{\mathtt{F}}(x,0) = \{x\}$.

**Voisinages :** Une partie $V \subseteq E$ est un **voisinage** d'un point $x \in E$ s'il existe un rayon $r > 0$ tel que la boule ouverte $B(x,r)$ soit entièrement contenue dans $V$. Autrement dit, $V$ est un voisinage de $x$ si et seulement si $x$ appartient à l'intérieur de $V$ (l'intérieur sera défini ci-dessous). On note $\mathcal{V}(x)$ (ou $\mathcal{V}_d(x)$ quand on veut préciser la métrique) l'ensemble de tous les voisinages de $x$. Les voisinages capturent l'idée de "proximité locale" autour d'un point : un voisinage est une région qui contient $x$ avec "un peu d'espace de manœuvre" autour de lui. Remarquons qu'un voisinage n'est pas nécessairement ouvert ; par exemple, $[0, 1]$ est un voisinage de $1/2$ dans $\mathbb{R}$, bien qu'il ne soit pas ouvert. Noter qu'un voisinage peut être très grand, comme $E$ elle-même est voisinage de chacun de ses points.

Une partie $U \subseteq E$ est dite **ouverte** si chaque point de $U$ est le centre d'une petite boule ouverte non-vide entièrement contenue dans $U$. Formellement, $\forall x \in U, \exists r>0$ tel que $B(x,r) \subseteq U$. Les caractérisations suivantes sont équivalentes :
- $U$ est ouvert ;

-$U$ est un voisinage de chacun de ses points ;

**Exercice :**Les boules ouvertes sont elles-mêmes des ouverts. 

$E$, le sous-ensemble vide, l'union quelconque et l'intersection finie d'ouverts sont des ouverts.

Un ensemble $F$ est **fermé** si son complémentaire $E \setminus F$ est ouvert. 

**Exercice :** Montrer que les ouverts (respectivement les fermés) d'un sous ensemble $A\subseteq (E,d)$, par rapport à la distance induite, sont exactement *les traces* des ouverts (respectivement des fermés) de $E$ (i.e. V ouvert dans $A$ si et seulement $V=U\cap A$ pour un certain ouvert $U$ de $E$.)


L'intersection quelconque et l'union finie de fermés sont des fermés. Le cercle unité $S^1$ dans $\mathbb{R}^2$ est un exemple de fermé (TD3).

Attention, "ouvert" et "fermé" ne sont pas des contraires. Une partie peut être les deux (dans l'espace discret, toutes les parties le sont) ou aucun des deux (comme $[0,1[$ dans $\mathbb{R}$). Dans un espace ultramétrique, on peut montrer que les boules ouvertes sont aussi fermées (TD3) !

**Les opérateurs topologiques :** Pour toute partie $A \subseteq E$, on peut définir trois régions fondamentales qui décomposent l'espace :

L'**intérieur** de $A$, noté $\mathring{A}$, est le plus grand ouvert contenu dans $A$. On peut le caractériser de manière équivalente comme l'ensemble des points dont $A$ est un voisinage :
$$\mathring{A} = \{x \in A \mid A \in \mathcal{V}(x)\} = \{x \in E \mid \exists r > 0, B(x,r) \subseteq A\}.$$

Il vient $A$ est ouvert si seulement si $A = \mathring{A}$.



L'**adhérence** (ou *fermeture* de $A$, notée $\bar{A}$, est le plus petit fermé contenant $A$. C'est l'ensemble des points "infiniment proches" de $A$, au sens où toute boule centrée en eux rencontre $A$ :
$$\bar{A} = \{x \in E \mid \forall r>0, B(x,r) \cap A \neq \emptyset\}.$$

L'**extérieur** de $A$, noté $\text{ext}(A)$, est l'intérieur du complémentaire : $\text{ext}(A) = \mathring{\overbrace{E \setminus A}}$. C'est l'ensemble des points qui sont "loin" de $A$, au sens où ils possèdent un voisinage entièrement disjoint de $A$.

La **frontière** de $A$, notée $\text{Fr}(A)$, est définie par $\text{Fr}(A) = \bar{A} \setminus \mathring{A}$. C'est l'ensemble des points qui sont à la fois infiniment proches de $A$ et de son complémentaire : ni intérieurs à $A$, ni extérieurs à $A$. Ces trois ensembles forment une partition de l'espace tout entier :
$$E = \mathring{A} \sqcup \text{Fr}(A) \sqcup \text{ext}(A).$$

L'exercice du TD3 demandant si $\overline{B(a,r)} = B_{\mathtt{F}}(a,r)$ est instructif. La réponse est non en général. Dans un espace discret, $\overline{B(x,1)} = \overline{\{x\}} = \{x\}$, mais $B_{\mathtt{F}}(x,1) = E$. 

**Exercice:** Cela devient vrai quand la distance en question est induite par un norme.

**Équivalence topologique de métriques :** Deux distances $d_1$ et $d_2$ sur un même ensemble $E$ sont dites **topologiquement équivalentes** si elles définissent la même famille de voisinages autour de chaque points, i.e. pour tout point $x \in E$, les systèmes de voisinages coïncident : $\mathcal{V}_{d_1}(x) = \mathcal{V}_{d_2}(x)$.  Cette notion est fondamentale car elle nous dit quand deux métriques décrivent "la même géométrie" du point de vue topologique.

En pratique, pour montrer que deux distances sont topologiquement équivalentes, on utilise souvent le critère suivant : pour tout $x \in E$ et tout $\varepsilon > 0$, il existe $\eta, \eta' > 0$ tels que
$$ B_{d_2}(x, \eta) \subseteq B_{d_1}(x, \varepsilon) \quad \text{et} \quad B_{d_1}(x, \eta') \subseteq B_{d_2}(x, \varepsilon). $$
Cela signifie que toute boule pour une distance contient une boule pour l'autre distance, et vice-versa (cf. TD2, Exercice 3).

Il vient $d_1$ et $d_2$ sont topologiquement équivalentes si elles définissent la même famille d'ouverts.

**Exemple fondamental :** Sur $\mathbb{R}^n$, les distances $d_1$, $d_2$, et $d_\infty$ sont topologiquement équivalentes. On peut le montrer en vérifiant que pour tout $x \in \mathbb{R}^n$, on a $\mathcal{V}_{d_1}(x) = \mathcal{V}_{d_2}(x) = \mathcal{V}_{d_\infty}(x)$. Par exemple, le TD2 (Exercice 4) démontre explicitement que $\mathcal{V}_{d_1}(0) = \mathcal{V}_{d_\infty}(0)$ sur $\mathbb{R}^2$, et par invariance par translation (ces distances proviennent de normes), cela s'étend à tout point de $\mathbb{R}^n$. Cette équivalence a des conséquences profondes : une suite converge pour l'une de ces distances si et seulement si elle converge pour les autres, et la limite est la même (cf. TD4, Exercice 4). Autrement dit, sur $\mathbb{R}^n$, la convergence coordonnée par coordonnée (pour $d_1$ ou $d_\infty$) équivaut à la convergence euclidienne (pour $d_2$).

### 3. Suites : Points d'Accumulation et Convergence

Les suites sont l'outil dynamique pour explorer la topologie d'un espace. Une suite est une fonction $u: \mathbb{N} \to E$. Les **termes** de $u$, sont notés $u_n$ ($\in E$), et la suite elle-même comme $(u_n)_{n\in \mathbb{N}}.$ 

Un point $a \in E$ est un **point d'accumulation** de la suite $(u_n)$ si la suite "revient" infiniment souvent aussi près que l'on veut de $a$. Formellement :
$$ \forall \varepsilon > 0, \forall N \in \mathbb{N}, \exists n \geq N \text{ tel que } d(u_n, a) < \varepsilon. $$
Cette définition est équivalente à la caractérisation ensembliste suivante :

**Remarque :**  $a$ est un point d'accumulation de $(u_n)$ si et seulement si pour tout $\varepsilon > 0$, l'ensemble des indices $\{ n \in \mathbb{N} \mid u_n \in B(a, \varepsilon) \}$ est infini.

**Proposition:** Soit $(u_n)$ une suite d'éléments de $(E, d)$ et soit $\ell \in E$. Les assertions suivantes sont équivalentes :

1.   Pour tout réel strictement positif $\varepsilon$, il existe un entier naturel $N$ tel que pour tout entier $n \geq N$, la distance entre $u_n$ et $\ell$ est strictement inférieure à $\varepsilon$. Mathématiquement, cela s'écrit :
    $$ \forall \varepsilon > 0, \exists N \in \mathbb{N}, \forall n \geq N, d(u_n, \ell) < \varepsilon. $$

2.   Pour tout réel strictement positif $\varepsilon$, l'ensemble des indices des termes de la suite qui n'appartiennent pas à la boule ouverte de centre $\ell$ et de rayon $\varepsilon$ est un ensemble fini. Autrement dit, pour tout $\varepsilon > 0$, l'ensemble $\{ n \in \mathbb{N} \mid u_n \notin B(\ell, \varepsilon) \}$ est fini. Cela signifie que l'image réciproque de toute boule centrée en $\ell$ est une partie **cofinie** de $\mathbb{N}$ (son complémentaire dans $\mathbb{N}$ est fini).



On dit qu'une suite $(u_n)$ d'un espace métrique $(E, d)$ **converge** vers un élément $\ell \in E$ si l'une des conditions équivalentes énoncées dans la proposition ci-dessus est satisfaite.

L'élément $\ell$ est alors appelé la **limite** de la suite $(u_n)$. Si une suite converge, sa limite est unique.


Si une suite $(u_n)$ converge vers une limite $\ell$, alors $\ell$ est son unique point d'accumulation. En effet, tout voisinage de $\ell$ contient une infinité de termes de la suite.

Il est important de noter que l'inverse n'est pas toujours vrai. Une suite peut posséder un unique point d'accumulation sans pour autant converger. Par exemple, la suite définie dans $\mathbb{R}$ par $u_n = 1/n$ si $n$ est impair et $u_n = n$ si $n$ est pair a $0$ comme unique point d'accumulation, mais elle ne converge pas car les termes de rang pair tendent vers l'infini.Le lien entre suites et topologie est intime :

*   **Caractérisation séquentielle de l'adhérence :** $x \in \bar{A}$ si et seulement si il existe une suite $(a_n)$ d'éléments de $A$ qui converge vers $x$.
*   **Caractérisation séquentielle des fermés :** Une partie $F$ est fermée si et seulement si les limites de toutes les suites convergentes d'éléments de $F$ appartiennent à $F$.

