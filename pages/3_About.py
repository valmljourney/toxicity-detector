import streamlit as st

st.sidebar.write("By Valmljourney")

st.title("About")

st.subheader("Introduction")
st.write("Hello and thank you so much for trying out my **Toxicity Detector**!")
st.write("My name is **Valmljourney** and this project is part of my journey of "\
            "learning Machine Learning. So feel free to give me a feedback on it!")


st.subheader("Datasets")
st.write("All the datasets that I used come from the *jigsaw-toxic-comment-classification-challenge* on **Kaggle**.")


st.subheader("ML Model")
st.write("The ML Model that I trained and used for this project is available on the Hugging Face website (valhgf/toxic-bert).")


st.subheader("Improvements compared to my previous project")
st.write("""
- Use of **LLM** (base-bert-uncased) combined with **fine-tuning**
- Added Jupyter notebooks to show the training and testing of the model
- Added an *Observations* page to show my thought process and how I built this project
- Use of an **API** (FastAPI) to request the prediction and the explanation on the website
""")