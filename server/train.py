
#Model PREDICTION iris

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import os
import pickle

# Chemin du répertoire dans lequel se trouve le script train.py
current_dir = os.path.dirname(os.path.abspath(__file__))
server_dir = os.path.join(current_dir, "server")
model_path = os.path.join(server_dir, "model.pkl")

iris= load_iris()

classifier = RandomForestClassifier()

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.1)
model = classifier.fit(X_train, y_train)

# Vérification si le répertoire "server" existe, sinon le créer
if not os.path.exists(server_dir):
    os.makedirs(server_dir)

# Sauvegarde du modèle entraîné
with open(model_path, "wb") as pickle_out:
    pickle.dump(model, pickle_out)