from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')


prompt=ChatPromptTemplate.from_messages([
    ("system", "You are a helful customer support agent."),
    ("human", "{input}")
])

chain=prompt | model

chain.invoke({"input": "Hello, how are you?"})

chain.invoke({"input": "Hello, how are you?"})
