from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.7)


st.header('Chat with OpenAI')

user_input = st.text_input('Enter your Prompt')

if st.button('Submit'):
    result = model.invoke(user_input)
    st.write(result.content)
