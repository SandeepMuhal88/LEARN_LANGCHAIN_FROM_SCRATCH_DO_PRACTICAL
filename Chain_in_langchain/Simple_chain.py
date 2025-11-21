# input->prompt->model->output->parser->final output that is required flow of langchain
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load API Key
load_dotenv()

# Load Model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0
)


# Load Prompt
prompt=PromptTemplate(
    template=" Generate 5 intersting facts about {Topic}",
    input_variables=["Topic"]
)

# # Load Parser
# parser=StrOutputParser()

# # Make Chain
# chain=prompt | model | parser
# result=chain.invoke({"Topic":"Black Hole"})
# print(result)
# chain.get_graph().print_ascii()

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'Topic':'cricket'})

print(result)

chain.get_graph().print_ascii()