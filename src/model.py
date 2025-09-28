from transformers import pipeline
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from lime.lime_text import LimeTextExplainer

model_name = "valhgf/toxic-bert"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)


class Model:
    def __init__(self):
        self.classifier = classifier
        self.model = model
        self.tokenizer = tokenizer