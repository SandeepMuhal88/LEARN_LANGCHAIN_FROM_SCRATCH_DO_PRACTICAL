from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model=ChatOpenAI(model_name='gpt-3.5-turbo',temperature=0.0)

# define the prompt template
t1=PromptTemplate(
    template='make a report about {Topic}',
    input_variables=['Topic']
)

t2=PromptTemplate(
    template='make a 5 lines of summary of {text}',
    input_variables=['text']
)

parser=StrOutputParser()
chain=t1 | model | parser | t2 | model | parser

result=chain.invoke({'Topic':'black hole'})
print(result)

