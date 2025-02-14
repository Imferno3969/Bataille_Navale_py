# Bataille Navale

## Description
Ce projet est une implémentation du jeu classique **Bataille Navale** en Python. Le jeu permet au joueur d'affronter une intelligence artificielle (IA) dans une bataille navale en plaçant stratégiquement ses bateaux et en tirant sur ceux de l'adversaire.

## Fonctionnalités
- Placement des bateaux par le joueur.
- Placement aléatoire des bateaux pour l'IA.
- Affichage des grilles de jeu (bateaux et tirs).
- Système de tir et détection des impacts.
- Calcul des scores en fonction des tirs réussis et manqués.
- Détermination automatique du gagnant.

## Règles du Jeu
- Chaque joueur dispose des navires suivants :
  - 1 Porte-avion (5 cases)
  - 1 Croiseur (4 cases)
  - 2 Contre-torpilleurs (3 cases)
  - 1 Sous-marin (2 cases)
- Les bateaux peuvent être placés horizontalement ou verticalement.
- Chaque joueur tire à tour de rôle.
- Un tir raté est marqué par `*`, un tir touché par `X`.
- Le jeu se termine lorsqu'un joueur a coulé tous les bateaux de l'adversaire ou a un score de 0.

## Installation
1. Clonez le dépôt GitHub :
   ```bash
   git clone https://github.com/Imferno3969/Bataille_Navale_py.git
   ```
2. Accédez au dossier du projet :
   ```bash
   cd bataille-navale
   ```
3. Exécutez le script :
   ```bash
   python bataille_navale.py
   ```

## Dépendances
Aucune bibliothèque externe n'est requise, seulement **Python 3**.

## Utilisation
1. Suivez les instructions affichées à l'écran pour placer vos bateaux.
2. Tirez en indiquant les coordonnées souhaitées.
3. L'IA joue automatiquement son tour.
4. Continuez jusqu'à ce qu'un joueur gagne la partie.

## Auteurs
- **Votre Nom**

## Licence
Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

