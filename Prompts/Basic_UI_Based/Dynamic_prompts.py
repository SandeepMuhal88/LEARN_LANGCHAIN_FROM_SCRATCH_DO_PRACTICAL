from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()

model= ChatGoogleGenerativeAI(model='gemini-2.5-flash')

st.header('DEEP AI FOR Research')

paper_input=st.selectbox('Select Research Paper Name ', ['Attention is all you need', 'BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding', 'GPT: A Framework for Building and Evaluating General Language Models'])
style_input=st.selectbox('Select Research Paper Style ', ['Beginner friendly', 'Technical', 'Code oriented','Mathematical'])
length_input=st.selectbox('Select Research Paper Length ', ['Short paragraph', 'Medium paragraph', 'Long paragraph'])

#Template
template = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}  
Explanation Length: {length_input}  
1. Mathematical Details:  
   - Include relevant mathematical equations if present in the paper.  
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
2. Analogies:  
   - Use relatable analogies to simplify complex ideas.  
If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
Ensure the summary is clear, accurate, and aligned with the provided style and length.
""",
input_variables=['paper_input', 'style_input', 'length_input'],
validate_template=True
)

#fill prompt template
prompt = template.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
})

if st.button('Generate'):
    result=model.invoke(prompt)     
    st.write(result.content)

