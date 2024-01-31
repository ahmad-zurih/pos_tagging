import streamlit as st
from nltk.tokenize import word_tokenize
import dill
from io import StringIO

nltk.download('punkt')

with open('hmm_tagger.pkl', 'rb') as f:
    loaded_tagger = dill.load(f)

uploaded_file = st.file_uploader("Choose a file to upload: ")

if uploaded_file is not None:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    string_data = stringio.read()
    tokens = word_tokenize(string_data)
    tagged_tokens = loaded_tagger.tag(tokens)
    output = ""
    for word, pos in tagged_tokens:
        output += word + " " + pos + "\n"

    st.download_button("download the output file", output, "resutls.txt")