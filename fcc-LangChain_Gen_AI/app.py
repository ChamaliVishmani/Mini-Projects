# Q&A Chatbot
import streamlit as st
import os
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# function to load openAI model and get response


def get_openai_response(question):
    llms = OpenAI(openai_api_key=os.environ["OPENAI_API_KEY"],
                  model_name="text-davinci-003", temperature=0.5)
    response = llm(question)


# initialize streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain application")

input = 
submit = st.button("Ask Question")

# if submit button is clicked
if submit:
    st.subheader("The response is:")
    st.write()
