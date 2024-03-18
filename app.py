import streamlit as st
import os
from summarization import *

st.title("Summarization of PDF file")


# Input for the OpenAI API key
key = st.text_input("Enter your unique key:", key="unique_key")

# Button to submit the API key
if st.button("Submit"):
    os.environ["OPENAI_API_KEY"] = key
    st.success("Key submitted successfully!")

    
# File uploader for the PDF file   
pdf_file = st.file_uploader("Press Browse to select PDF file", type="pdf", key="pdf_uploader")


# Button to trigger the summarization process
if st.button("Summarize PDF"):
    if pdf_file is not None:
        summary, cost = summarizer(pdf_file)
        st.write("Summarized text:")
        st.write(summary)
        st.write("Query cost:")
        st.write(cost)
    else:
        st.error("Please upload a PDF file.")
