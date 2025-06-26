
# Test Technique - Pipotron (Xerfi)

Ce projet est une réponse au test technique Python proposé par Xerfi. Il a pour objectif de vérifier si une phrase donnée respecte une structure de "pipotron", c’est-à-dire une phrase générée automatiquement par assemblage de composants définis.

---

## Structure du projet

Le projet est organisé de manière modulaire pour faciliter la compréhension et l'exécution :

```
pipotron-xerfi/
├── pipotron/                 # Contient la logique principale (my_function, generate_random_phrase)
│   ├── core.py
│   └── __init__.py
│
├── streamlit/               # Interface utilisateur web (optionnelle)
│   └── app.py
│
├── run.py                   # Interface console interactive
├── test.py                  # Tests automatiques simples
├── requirements.txt         # Liste des dépendances
└── README.md                # Ce fichier
```

---

## Installation

Créer un environnement virtuel (optionnel mais recommandé), puis installer les dépendances :

```bash
python -m venv venv
source venv/bin/activate      # Pour Linux/Mac
# .\venv\Scripts\activate  # Pour Windows

pip install -r requirements.txt
```

---

## Deux modes d'utilisation

### 1. Mode console (principal)

Ce mode permet de tester l’algorithme pas à pas depuis le terminal. Vous serez invité à entrer les composants et la phrase à valider.

```bash
python run.py
```

C'est la manière la plus directe d'interagir avec l’algorithme.

---

### 2. Interface web avec Streamlit (optionnel)

Ce mode offre une interface interactive :
- possibilité d’ajouter les composants à la main ou depuis un fichier `.json` ou `.txt`
- génération automatique de phrases
- vérification avec ou sans distinction de casse
- messages explicites en cas d'erreur

```bash
streamlit run streamlit/app.py
```

Ce mode reste facultatif mais illustre une intégration utilisateur plus poussée.

---

## Tests automatiques

Un fichier de test est fourni pour valider les cas courants.

```bash
pytest test.py
```

Tous les tests doivent passer.

---

## Remarques importantes

- Ce projet ne vérifie pas la grammaire naturelle des phrases, uniquement leur conformité à une structure définie (pipotron).
- Une tentative d’intégration de la bibliothèque `language-tool-python` a été testée pour vérifier la grammaire, mais a été abandonnée pour des raisons de simplicité, de poids et parce que cela dépassait le cadre de l'exercice.
- La logique intégrée tient compte des règles d'espacement autour des signes de ponctuation :
  - pas d’espace avant les signes comme `.` ou `,`
  - une espace obligatoire avant les signes comme `!`, `?`, `:`, `;`
  - la phrase doit obligatoirement se terminer par un signe de ponctuation
- Aucun fichier d’environnement virtuel n’est inclus.
- Le code est conçu pour être exécuté immédiatement, sans configuration supplémentaire.

---

## Auteur

Abdessalem Djoudi  
Mail : abdessalem.djoudi@edu.dsti.institute  
GitHub : https://github.com/djoudi92
