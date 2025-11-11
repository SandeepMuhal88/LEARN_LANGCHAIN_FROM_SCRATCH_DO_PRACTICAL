from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint,HuggingFacePipeline
from dotenv import load_dotenv

load_dotenv()
# When we want to store file other location
# os.environ["TRANSFORMERS_CACHE"]="D:\Project-to-learn\Learn_Langchain\Lanchain_Models\Using_Hugging_face\cache"
# But when CWD is Automatically set to the location of the script

llms=HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "temperature":0.7,
        "max_new_tokens":32,
    }
)

model=ChatHuggingFace(llm=llms)

result=model.invoke("What is capital of India")

print(result.content)