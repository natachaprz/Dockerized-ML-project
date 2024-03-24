# A Dockerized-ML-project
This project aims to create a Streamlit application serving as a user interface for making predictions with a pre-trained ML model.

## Project Structure
The project is organized as follows:
- `server/`: Contains the `train.py` script for training the model and the `API.py` script for the FastAPI server.
- `client/`: Contains the `app.py` script for the Streamlit user interface.
- `requirements.txt`: Python dependencies required for both server and client.

## Setup
1. Clone this repository to your local machine: `git clone https://github.com/natachaprz/Dockerized-ML-project.git`
2. Run `docker compose up --build`to build and run the Docker image.
3. Access `http://localhost:8501` to use the Streamlit application.

## Features
- The `train.py` script trains an Iris classification model using scikit-learn and saves the trained model to a `model.pkl` file.
- The FastAPI server exposes a POST endpoint `/predict` for making predictions using the trained model.
- The Streamlit client application allows the user to input Iris features and see the model's prediction
