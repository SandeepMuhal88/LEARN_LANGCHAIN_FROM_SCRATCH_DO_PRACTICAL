from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llms=HuggingFaceEndpoint(
    repo_id="moonshotai/Kimi-K2-Thinking",
    task="text-generation",
)

model=ChatHuggingFace(llm=llms)

result=model.invoke("What is the capital of America")

print(result.content)
