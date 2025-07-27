# Make sure to install required packages using the terminal:
#pip install langchain openai streamlit
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

llm = ChatOpenAI(
    model="llama-3.1-8b-instant", 
    temperature=1, 
    openai_api_key="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",
    openai_api_base="https://api.groq.com/openai/v1")

p = st.text_input("Enter your prompt: ")
response = llm.predict_messages([HumanMessage(content=p)])
st.write(response.content)


