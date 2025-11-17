from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

from urllib3 import response

load_dotenv()

HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Chat model from HuggingFace
llms=HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "temperature":0.7,
        "max_new_tokens":32,
    }
)

model=ChatHuggingFace(llm=llms)

template_1=PromptTemplate(
    template='write a deatiled report on {Topic}',
    input_variables=['Topic']
)

template_2=PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

# Create a parsers
parser=StrOutputParser()
# Make chain

chain=template_1 | model | parser | template_2 | model | parser 

response   =chain.invoke({'Topic':'black hole'})
print(response)
