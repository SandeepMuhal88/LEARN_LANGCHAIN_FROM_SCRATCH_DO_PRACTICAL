from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()
# When we want to store file other location
# os.environ["TRANSFORMERS_CACHE"]="D:\Project-to-learn\Learn_Langchain\Lanchain_Models\Using_Hugging_face\cache"
# But when CWD is Automatically set to the location of the script

llms=HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "temperature":0.0,
        "max_new_tokens":5000,
    }
)

model=ChatHuggingFace(llm=llms)

#fist prompt- detailed report
template_1=PromptTemplate(
    template='write a deatiled report on {Topic}',
    input_variables=['Topic']
)

#2 promptsummary 
template_2=PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

p1=template_1.invoke({'Topic':'black hole'})
response=model.invoke(p1)
p2=template_2.invoke({'text':response.content})

result=model.invoke(p2)
print(result.content)