import streamlit as st
from nltk.tokenize import word_tokenize
import dill

nltk.download('punkt')

with open('hmm_tagger.pkl', 'rb') as f:
    loaded_tagger = dill.load(f)

short_text = st.text_input("Please insert a sentence to get the POS tag for it: ")

if short_text:
    tokens = word_tokenize(short_text)
    tagged = loaded_tagger.tag(tokens)
    html_result = ""
    for word, pos in tagged:
        html_result += f"<span style='color: blue;'>{word} </span> <span style='color: red;'> {pos} </span>"
    st.markdown(html_result, unsafe_allow_html=True)
    