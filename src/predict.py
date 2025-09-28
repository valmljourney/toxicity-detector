from src.model import *
import numpy as np

def predict_text(ml_model: Model, text: str):
    result = ml_model.classifier(text)[0]
    if result['label'] == 'LABEL_0':
        return ('Not Toxic', result['score'])
    else:
        return ('Toxic', result['score'])
    

def explain_text(ml_model: Model, text: str):
    class_names = ["non_toxic", "toxic"]
    
    def lime_predict_proba(texts):
        results = ml_model.classifier(texts, return_all_scores=True)
        return np.array([[r['score'] for r in res] for res in results])
    
    lime_explainer = LimeTextExplainer(class_names=class_names)
    
    exp = lime_explainer.explain_instance(text, lime_predict_proba, num_features=10, num_samples=100, labels=[0, 1])
    
    # Contribution for the 'Toxic' class
    return exp.domain_mapper.map_exp_ids(exp.as_map()[1])
 