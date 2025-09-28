import streamlit as st

st.sidebar.write("By Valmljourney")

st.title(":violet[Observations]")

st.subheader("Training the ML model")

p1 = """
At first, I didn't know that fine-tuning a model was that **:orange[power demanding]**, but I realised this when training on the whole dataset on my own pc.
\nSo I significantly reduced the dataset size (**:red[150k] --> :green[6k]**).
\nIt worked but I started to see **overfitting** and my results in real usage were **not very convincing**.
""" 
st.write(p1)

st.subheader("Improving the ML model: Part 1")
p2 = """
I tried to fix this by doing those **:blue[4 different things]**:
- Take a bigger dataset (**:red[6k] --> :blue[10k]**)
- Change the threshold of what is considered as **:red[toxic]**  -->  Not very efficient since my dataset is very **:blue[unbalanced]**
- Balance the dataset (50/50 toxic/non-toxic)  -->  Good scores for the training but bad ones for the **:blue[testing]**
- Doing weighted loss  -->  Subtle improvement for the testing, but **:blue[nothing significant]**.
"""
st.write(p2)
"""
At the end, those were the results I had on the training:
| Epoch | Training Loss | Validation Loss | Accuracy | F1    | Precision | Recall |
| ----- | ------------- | --------------- | -------- | ----- | --------- | ------ |
| 1     | 0.1235        | 0.1434          | 0.958    | 0.744 | 0.910     | 0.629  |
| 2     | 0.0548        | 0.1743          | 0.953    | 0.761 | 0.750     | 0.773  |
| 3     | 0.0260        | 0.2062          | 0.961    | 0.787 | 0.837     | 0.742  |

\nWith the training loss decreasing and the validation loss increasing (up to **:blue[20%]**), we can see a pretty significant start of **:blue[overfitting]**.

\nThe biggest problem at that moment is that my ML model wouldn't be sometimes coherent, due to the fact that the dataset was **:blue[very small]**.
"""


st.subheader("Improving the ML model: Part 2")
p3 = """
In order to significantly improve my ML model I decided to use **:rainbow[Google Colab]**.
\nThis allowed me to trained on the whole dataset and it significantly improved my training scores.
\nFrom the improvement technics that I tried previously, I kept the **:rainbow[weighted loss]**, but I didn't change the **threshold** nor **balanced the dataset**.

\nNew results:
Epoch | Training Loss | Validation Loss | Accuracy | F1   | Precision | Recall |
------|---------------|-----------------|----------|------|-----------|------- |
1     | 0.0948        | 0.0894          | 0.968    | 0.829| 0.864     | 0.797  |
2     | 0.0654        | 0.1062          | 0.968    | 0.836| 0.832     | 0.840  |
3     | 0.0468        | 0.1126          | 0.968    | 0.832| 0.842     | 0.822  |

\nWe can see here that we don't have overfitting compared to the previous training.
\nMost importantly, my model is now **:rainbow[coherent]** for most cases and understands way better the **:rainbow[context]**, making it totally usable in **:rainbow[real life application]**.

\nI also added an **:rainbow[explanation]** button that highlights which words are responsible for flagging toxic, using **:green[LIME]**.
I also tried occlusion/masking but it wasn't very efficient so I stuck to LIME.

"""
st.write(p3)


st.subheader("Room for improvements")
p4 = """
- Only detects **:orange[toxic words]**:
When looking at the words' **:green[influence score]** given by **:green[LIME]**, I noticed that for toxic detection, my ML model gives scores close to **:orange[1]** for **:orange[toxic]** words but
gives scores close to **:orange[0]** for **:orange[non-toxic]** words (while the range is **:orange[(-1, 1)]**).
Hence, my ML model flag toxic when it detects toxic words
, but flag non-toxic when it **:orange[doesn't]** detect toxic words.

- It doesn't understand **:orange[negation]**:
*I don't hate you* --> detected as :red[toxic]

- It doesn't understand **:orange[sarcasm]**:
*You're so dumb bro haha* --> detected as :red[toxic]
"""
st.markdown(p4)
