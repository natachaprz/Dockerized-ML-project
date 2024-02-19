# Full-stack-Dockerized-ML-project
Ce projet vise à créer une application Streamlit qui sert d'interface utilisateur pour effectuer des prédictions sur un modèle ML pré-entraîné.

## Structure du Projet
Le projet est organisé comme suit :
- `server/`: Contient le script `train.py` pour entraîner le modèle et le script `API.py` pour le serveur FastAPI.
- `client/`: Contient le script `app.py` pour l'interface utilisateur Streamlit.
- `requirements.txt`: Les dépendances Python nécessaires pour le serveur et le client.

## Installation et Utilisation
1. Clonez ce dépôt sur votre machine locale.
2. Tapez 'docker compose up --build' pour construire et exécuter l'image Docker.
6. Accédez à "http://localhost:8501" pour accéder à l'application Streamlit.

## Fonctionnalités
- Le script `train.py` entraîne un modèle de classification d'Iris en utilisant scikit-learn et sauvegarde le modèle entraîné dans un fichier `model.pkl`.
- Le serveur FastAPI expose un endpoint POST `/predict` qui prend en charge les prédictions en utilisant le modèle entraîné.
- L'application client Streamlit permet à l'utilisateur de saisir les caractéristiques de l'Iris et de voir la prédiction du modèle.
