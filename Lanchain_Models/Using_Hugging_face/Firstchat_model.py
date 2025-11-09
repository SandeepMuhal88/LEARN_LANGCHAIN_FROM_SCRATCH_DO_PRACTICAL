from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

from Learn_Langchain.Lanchain_Models.LLMS.tempCodeRunnerFile import llm

load_dotenv()

llms=HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
)

model=ChatHuggingFace(llm=llms)

result=model.invoke("What is capital of India")

print(result.content)