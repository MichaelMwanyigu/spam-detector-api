from fastapi import FastAPI
from pydantic import BaseModel
from src.schemas.message_schemas import MessageRequest, MessageResponse
import joblib

#Loading the model
MODEL_PATH = "src/model/spam_model.joblib"
spam_model = joblib.load(MODEL_PATH)


#Creating a Fast API app
app = FastAPI(title = "API for spam model")

@app.get("/")
def home():
    response = "Hello! Welcome to the spam model api"
    return MessageResponse(message = response)
    


@app.post("/predict")
def predict(request: MessageRequest):
    spam_prediction = spam_model.predict([request.message])[0]
    return MessageResponse(message = spam_prediction)






