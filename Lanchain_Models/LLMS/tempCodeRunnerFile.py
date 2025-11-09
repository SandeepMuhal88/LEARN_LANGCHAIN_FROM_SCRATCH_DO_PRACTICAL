from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
# ... load_dotenv() is still needed

llm = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

# For Chat models, it's best practice to pass a list of messages
result = llm.invoke([
    HumanMessage(content="What is the capital of India")
])

print(result.content)