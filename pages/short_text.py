import dill
import streamlit as st
from nltk.tokenize import word_tokenize
from io import StringIO
import nltk

nltk.download('punkt')

st.set_page_config(
        page_title="POS Tagger - Tag short text",
)


# Load the trained model from the file
with open('hmm_tagger.pkl', 'rb') as f:
    loaded_tagger = dill.load(f)


text = st.text_input("Insert a text to get the POS tagging")

if text:
    tokens = word_tokenize(text)
    tagged_sentence = loaded_tagger.tag(tokens)
    results_html = ""
    for word, tag in tagged_sentence:
        results_html += f"<span style='color: blue;'>{word}</span> <span style='color: red;'>{tag}</span> "

    st.markdown(results_html, unsafe_allow_html=True)
    