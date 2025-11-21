from langchain_huggingface_endpoint import HuggingFaceEndpoint
from langchain_chat_huggingface import ChatHuggingFace
from langchain.prompts import PromptTemplate
from langchain.output_parsers import JsonOutputParser
from dotenv import load_dotenv


load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)
