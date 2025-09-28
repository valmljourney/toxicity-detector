import streamlit as st
import requests

st.sidebar.write("By Valmljourney")

st.title(":red[Toxic]ity Detector")

input = st.text_input("Enter a text: ")

if input:
    json_input = {"text": input}
    res = requests.post(url="http://127.0.0.1:8000/predict", json=json_input)
    if res.ok:
        output = res.json()
        mapping = {"Toxic": ":red[Toxic]", "Not Toxic": ":green[Not Toxic]"}
        st.write(f"Output: [{mapping[output[0]]} | {output[1]}]")

        explain_button = st.button("Explanation with **:green[LIME]**")
        if explain_button:
            response = requests.post(url="http://127.0.0.1:8000/explain", json=json_input)
            if response.ok:
                words_weights = response.json()
                explanation = {}
                for word, weight in words_weights:
                    if weight < 0.3:
                        explanation[word] = "not_toxic"
                    else:
                        explanation[word] = "toxic"
                        
                highlighted = ""
                for word in input.strip().split(' '):
                    if word not in explanation or explanation[word] == "not_toxic":
                        highlighted += f":green[{word}] "
                    else:
                        highlighted += f":red[{word}] "
                
                st.write(highlighted)