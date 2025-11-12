from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import load_prompt
import streamlit as st
load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')


st.header('DEEP AI FOR Research')

paper_input=st.selectbox('Select Research Paper Name ', ['Attention is all you need', 'BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding', 'GPT: A Framework for Building and Evaluating General Language Models'])
style_input=st.selectbox('Select Research Paper Style ', ['Beginner friendly', 'Technical', 'Code oriented','Mathematical'])
length_input=st.selectbox('Select Research Paper Length ', ['Short paragraph', 'Medium paragraph', 'Long paragraph'])

prompt_template=load_prompt('template.json')

filled_prompt_template = prompt_template.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
})

if st.button('Generate'):
    result=model.invoke(filled_prompt_template)
    st.write(result.content)