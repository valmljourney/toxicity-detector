import pandas as pd
import streamlit as st

st.sidebar.write("By Valmljourney")

def clean_df(df: pd.DataFrame):
    df = df[["comment_text","toxic"]]
    df = df.drop_duplicates(["comment_text"])
    df = df[df["toxic"] != -1]
    df["comment_text"] = df["comment_text"].str.strip()
    df["comment_text"] = df["comment_text"].str.lower()
    df = df[df["comment_text"].str.len() > 0]
    return df

train_df = pd.read_csv('datasets/train.csv')

test_df = pd.read_csv('datasets/test.csv')
labels_df = pd.read_csv('datasets/test_labels.csv')
test_df = pd.merge(test_df, labels_df, on='id')

train_df = clean_df(train_df)
test_df = clean_df(test_df)

st.title(":green[Datasets]")
st.subheader("Training Dataset (extract)")
st.write(train_df)
st.subheader("Test Dataset (extract)")
st.write(test_df)