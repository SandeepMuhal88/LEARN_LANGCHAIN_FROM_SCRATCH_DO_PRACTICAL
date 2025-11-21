import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Setup the Model
model = ChatOpenAI(model="gpt-4o-mini")

# 2. Create a Prompt Template
prompt = ChatPromptTemplate.from_template("Explain {topic} in one sentence.")

# 3. Create the Output Parser (Converts message object to string)
parser = StrOutputParser()

# 4. Build the Chain using LCEL Pipes (|)
basic_chain = prompt | model | parser

# 5. Invoke
response = basic_chain.invoke({"topic": "Quantum Entanglement"})
print(response)