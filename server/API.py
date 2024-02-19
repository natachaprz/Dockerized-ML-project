
#Creating the API
import pickle
import logging
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
#from models.iris import Iris

app = FastAPI()

with open("server/model.pkl", "rb") as pickle_in:
    model = pickle.load(pickle_in)


class Iris(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float



@app.post("/predict")
def predict_iris(iris: Iris):
    logging.info("Received prediction request for Iris data: %s", iris.model_dump())

    try:
        prediction = model.predict([[iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width]])
        iris_types = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
        predicted_type = iris_types[prediction[0]]

        return {"iris_type": predicted_type}
    except Exception as e:
        logging.error("Prediction failed: %s", str(e))
        raise HTTPException(status_code=500, detail="Prediction failed, please check your input data.")

