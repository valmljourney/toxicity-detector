import streamlit as st

st.sidebar.write("By Valmljourney")

st.title(":violet[Observations]")

st.subheader("Training the ML model")

p1 = """
At first, I didn't know that fine-tuning a model was that **power demanding**, but I realized this when training on the whole dataset on my own pc.
\nSo I significantly reduced the dataset size (**150k --> 6k**).
\nIt worked but I started to see **overfitting** and my results in real usage were **not very convincing**.
""" 
st.write(p1)

st.subheader("Improving the ML model: Part 1")
p2 = """
I tried to fix this by doing those **4 different things**:
- Take a bigger dataset (**6k --> 10k**)
- Change the threshold of what is considered as **toxic**  -->  Not very efficient since my dataset is very **unbalanced**
- Balance the dataset (50/50 toxic/non-toxic)  -->  Good scores for the training but bad ones for the **testing**
- Doing weighted loss  -->  Subtle improvement for the testing, but **nothing significant**.
"""
st.write(p2)
"""
At the end, those were the results I had on the training:
| Epoch | Training Loss | Validation Loss | Accuracy | F1    | Precision | Recall |
| ----- | ------------- | --------------- | -------- | ----- | --------- | ------ |
| 1     | 0.1235        | 0.1434          | 0.958    | 0.744 | 0.910     | 0.629  |
| 2     | 0.0548        | 0.1743          | 0.953    | 0.761 | 0.750     | 0.773  |
| 3     | 0.0260        | 0.2062          | 0.961    | 0.787 | 0.837     | 0.742  |

\nWith the training loss decreasing and the validation loss increasing (up to **20%**), we can see a pretty significant start of **overfitting**.

\nThe biggest problem at that moment is that my ML model wouldn't be sometimes coherent, due to the fact that the dataset was **very small**.
"""


st.subheader("Improving the ML model: Part 2")
p3 = """
In order to significantly improve my ML model I decided to use **Google Colab**.
\nThis allowed me to train on the whole dataset and it significantly improved my training scores.
\nFrom the improvement techniques that I tried previously, I kept the **weighted loss**, but I didn't change the **threshold** nor **balanced the dataset**.

\nNew results:
Epoch | Training Loss | Validation Loss | Accuracy | F1   | Precision | Recall |
------|---------------|-----------------|----------|------|-----------|------- |
1     | 0.0948        | 0.0894          | 0.968    | 0.829| 0.864     | 0.797  |
2     | 0.0654        | 0.1062          | 0.968    | 0.836| 0.832     | 0.840  |
3     | 0.0468        | 0.1126          | 0.968    | 0.832| 0.842     | 0.822  |

\nWe can see here that we don't have overfitting compared to the previous training.
\nMost importantly, my model is now **coherent** for most cases and understands way better the **context**, making it totally usable in **real life application**.

\nI also added an **explanation** button that highlights which words are responsible for flagging toxic, using **LIME**.
I also tried occlusion/masking but it wasn't very efficient so I stuck to LIME.

"""
st.write(p3)


st.subheader("Room for improvements")
p4 = """
- Only detects **toxic words**:
When looking at the words' **influence score** given by **LIME**, I noticed that for toxic detection, my ML model gives scores close to **1** for **toxic** words but
gives scores close to **0** for **non-toxic** words (while the range is **(-1, 1)**).
Hence, my ML model flags toxic when it detects toxic words
, but flags non-toxic when it **doesn't** detect toxic words.

- It doesn't understand **negation**:
*I don't hate you* --> detected as toxic

- It doesn't understand **sarcasm**:
*You're so dumb bro haha* --> detected as toxic
"""
st.markdown(p4)
