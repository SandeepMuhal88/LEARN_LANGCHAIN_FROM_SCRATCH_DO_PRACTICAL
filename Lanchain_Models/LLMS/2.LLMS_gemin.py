from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# Initialize the Gemini model
# Note: 'gemini-2.5-flash' is the recommended model for general tasks
llm = GoogleGenerativeAI(model='gemini-2.5-flash')

result = llm.invoke("What is the deep learning")

# The result might be a string or a ChatMessage object depending on the class used,
# but for a simple LLM model, it's typically a string you can print directly.
print(result)