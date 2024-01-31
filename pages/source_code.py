import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
        page_title="POS Tagger - Code",
)



with open("hmm_nltk.html", "r") as f:
    html_page = f.read()


components.html(html_page, height=6000,)