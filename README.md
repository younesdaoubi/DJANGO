# DJANGO

# Site de Vente Immobilière avec Django

## Description
Ce projet est un site de vente immobilière développé en Python avec le framework Django. Il permet aux utilisateurs de s'inscrire, de se connecter, de gérer leur profil, de publier des annonces immobilières, et bien plus encore.

## Fonctionnalités

### 1. Inscription
- Les utilisateurs peuvent s'inscrire via un formulaire d'inscription.
- Champs requis : pseudo, mot de passe (2x), email.
- Si l'utilisateur existe déjà, la création de compte est impossible.

### 2. Connexion / Déconnexion
- Les utilisateurs peuvent se connecter à leur compte et se déconnecter à tout moment.

### 3. Gestion de la page de profil (CRUD)
- L'utilisateur peut modifier son pseudo, son email ou sa photo de profil directement depuis sa page de profil.

### 4. Gestion des publications (Update / Delete)
- Les utilisateurs peuvent mettre à jour ou supprimer leurs annonces via un formulaire de modification des champs.

### 5. Pagination
- La pagination est implémentée pour une navigation fluide entre les pages d'annonces.

### 6. Système de récupération de mot de passe
- En cas de mot de passe oublié, l'utilisateur peut réinitialiser son mot de passe via un système de récupération par email (Gmail).

### 7. Système de recherche d'annonces
- Recherche d'annonces via un mot-clé dans le titre ou le contenu des annonces.
- Les résultats sont affichés sur la page `search.html`.

### 8. WatchList
- Les utilisateurs peuvent sauvegarder leurs annonces préférées dans une WatchList, accessible depuis leur profil sous l'onglet "Favoris".

### 9. Carte GPS
- Affichage de la localisation des annonces sur une carte GPS pour faciliter la recherche géographique.

## Installation

### Prérequis
- Python 3.x
- Django
- PyCharm ou autre éditeur de code