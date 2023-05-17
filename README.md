# Keycloak Authentication Project with Django

This project is a Django web application that uses Keycloak for user authentication. It also incorporates two-factor authentication (2FA) using an OTP (One-Time Password) and an app like Authenticator. The project includes synchronization with Keycloak for creating and updating users in the Django database.

## Features
- User authentication via Keycloak.
- Two-Factor Authentication (2FA) with OTP and an app like Authenticator.
- Synchronization of users between Keycloak and Django.
- Updating user profile information in Django and Keycloak.
- Verification of user email addresses.
- Extended user profile with additional fields like address, phone, etc. (in development).
- REST API for accessing user information (upcoming).

## Prerequisites
- Python 3.8+
- Django 3.2+
- A running Keycloak server.

## Installation
1. Clone this repository.
2. Install the dependencies with `pip install -r requirements.txt`.
3. Configure the Keycloak connection parameters in `settings.py`.
4. Run the migrations with `python manage.py migrate`.
5. Start the server with `python manage.py runserver`.

## Usage
When a user logs in for the first time via Keycloak, a new user is created in the Django database with the information provided by Keycloak. Subsequent logins will update the user's information in Django based on the information from Keycloak.

Users can update their profile information in Django. The changes will also be reflected in Keycloak.

## Contribution
Contributions are welcome. Feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.




# Projet d'authentification Keycloak avec Django

Ce projet est une application web Django qui utilise Keycloak pour l'authentification des utilisateurs. Il intègre également l'authentification à deux facteurs (2FA) en utilisant un OTP (One-Time Password) et une application comme Authenticator. Le projet inclut une synchronisation avec Keycloak pour la création et la mise à jour des utilisateurs dans la base de données Django.

## Caractéristiques
- Authentification des utilisateurs via Keycloak.
- Authentification à deux facteurs (2FA) avec OTP et une application comme Authenticator.
- Synchronisation des utilisateurs entre Keycloak et Django.
- Mise à jour des informations de profil utilisateur dans Django et Keycloak.
- Vérification de l'adresse e-mail des utilisateurs.
- Profil utilisateur enrichi avec des champs additionnels comme adresse, téléphone, etc (en cours de développement).
- API REST pour accéder aux informations de l'utilisateur (à venir).

## Prérequis
- Python 3.8+
- Django 3.2+
- Un serveur Keycloak en cours d'exécution.

## Installation
1. Cloner ce dépôt.
2. Installer les dépendances avec `pip install -r requirements.txt`.
3. Configurez les paramètres de connexion à Keycloak dans `settings.py`.
4. Effectuez les migrations avec `python manage.py migrate`.
5. Lancez le serveur avec `python manage.py runserver`.

## Utilisation
Lorsqu'un utilisateur se connecte pour la première fois via Keycloak, un nouvel utilisateur est créé dans la base de données Django avec les informations fournies par Keycloak. Les connexions suivantes mettront à jour les informations de l'utilisateur dans Django en fonction des informations de Keycloak.

Les utilisateurs peuvent mettre à jour leurs informations de profil dans Django. Les modifications seront également répercutées dans Keycloak.

## Contribution
Les contributions sont les bienvenues. N'hésitez pas à ouvrir un problème ou à soumettre une demande d'extraction.

## Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.
