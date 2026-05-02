# Tâches proposées après revue rapide du code

## 1) Coquille typographique
**Constat**
- Le champ affiché dans la page d’accueil contient `1,232 Rec.Yards` ; l’abréviation et la ponctuation sont incohérentes avec le reste des libellés (ex. `Yds/R`).

**Tâche**
- Uniformiser le libellé en `1,232 Receiving Yards` (ou `1,232 Rec Yds`) pour améliorer la lisibilité.
- Vérifier les autres libellés statistiques de `home.html` pour harmoniser style, ponctuation et unités.

## 2) Correction de bug
**Constat**
- Le fichier de tests Django (`NFL/tests.py`) contient du code de template HTML/Jinja au lieu de tests Python, ce qui casse la structure attendue pour l’exécution des tests.

**Tâche**
- Restaurer `NFL/tests.py` en module Python valide.
- Déplacer le contenu HTML dans le bon template (ou le supprimer si doublon), puis exécuter `python manage.py test`.
- Ajouter une protection CI pour refuser tout fichier `tests.py` non importable.

## 3) Commentaire / documentation à corriger
**Constat**
- Le commentaire généré par défaut `# Create your tests here.` est obsolète et trompeur compte tenu du contenu actuel du fichier.

**Tâche**
- Remplacer ce commentaire par une docstring explicite décrivant les tests attendus pour les vues (`home`, `offense`, `defense`) et les cas de non-régression.
- Ajouter un court `README` de l’app `NFL/` (ou une section dédiée) expliquant la stratégie de test.

## 4) Amélioration de test
**Constat**
- Aucun test ne valide les vues `offense`/`defense` qui dépendent d’appels réseau dans `NFL/data_scrape/*.py`.

**Tâche**
- Écrire des tests unitaires de vues avec mocking (`unittest.mock.patch`) pour simuler `offense_func` et `defense_func` sans réseau.
- Vérifier : code HTTP 200, template rendu, et présence des clés de contexte (`qbs`, `rbs`, `wrs`, `tackles`, `ints`).
- Ajouter un test de gestion d’erreur (ex. exception scraping) et comportement attendu (message utilisateur ou fallback).
