from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0
)

prompt_01=PromptTemplate(
    template="Generate Detailed report on  {Topic}",
    input_variables=["Topic"]
)

prompt_02=PromptTemplate(
    template="Generate a 5 points summary from the following text \n {text}",
    input_variables=["text"]
)


parser=StrOutputParser()

chain=prompt_01 | model | parser | prompt_02 | model | parser

result=chain.invoke({"Topic":"AI"})
print(result)
chain.get_graph().print_ascii()
