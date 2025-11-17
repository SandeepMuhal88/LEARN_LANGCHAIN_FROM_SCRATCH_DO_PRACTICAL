from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

from Learn_Langchain.Lanchain_Models.LLMS.tempCodeRunnerFile import llm

load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)

result=model.invoke("What is capital of India")

print(result.content)