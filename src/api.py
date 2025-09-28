from fastapi import FastAPI
from pydantic import BaseModel
import src.predict as pred
import src.model as md

app = FastAPI()

class TextInput(BaseModel):
    text: str

ml_model = md.Model()

@app.post("/predict")
def predict_toxicity(input: TextInput):
    return pred.predict_text(ml_model, input.text)

@app.post("/explain")
def explain_result(input: TextInput):
    return pred.explain_text(ml_model, input.text)