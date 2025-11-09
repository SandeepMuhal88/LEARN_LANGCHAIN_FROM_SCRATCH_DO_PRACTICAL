from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llms=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

result = llms.invoke("What is capital of India",temperature=0.7,max_tokens=40)

print(result.content)