# from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
# from langchain.output_parsers import StructuredOutputParser,ResponseSchema

# load_dotenv()

# llm= HuggingFaceEndpoint(
#     repo_id="google/gemma-2-2b-it",
#     task="text-generation"
# )

# model= ChatHuggingFace(llm=llm)

# parser= StructuredOutputParser(
#     return_id=True,
#     response_schemas=[
#         ResponseSchema(name="name", description="The name of the person"),
#         ResponseSchema(name="age", description="The age of the person"),
#         ResponseSchema(name="gender", description="The gender of the person"),
#     ]
# )

# format_instructions = parser.get_format_instructions()

# template = PromptTemplate(
#     input_variables=["name", "age", "gender"],
#     partial_variables={"format_instructions": format_instructions},
#     template="""
#     {format_instructions}
    
#     Name: {name}
#     Age: {age}
#     Gender: {gender}
#     """
# )


# chain = template | model | parser

# result = chain.invoke({"name": "John", "age": 30, "gender": "male"})

# print(result)

from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name='fact_1', description='    Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give 3 fact about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)