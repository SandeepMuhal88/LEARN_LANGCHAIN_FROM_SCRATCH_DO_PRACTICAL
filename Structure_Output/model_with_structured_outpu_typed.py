# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv
# from typing import TypedDict
# load_dotenv()

# model=ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')


#**************************** Schema*****************************************
# class Review(TypedDict):

#     summary: str
#     sentiment: str

# structured_output=model.with_structured_output(Review)

# response=structured_output.invoke("""The hardware is grate but software feels bloated.
# There are too many preinstalled apps That i can't remove. Also UI like outdated compare to other brands.
# Hoping software will get updated soon. and fix that""")

# print(response)
# print(response['summary']) 
# print(response['sentiment'])


#**************************** Model*****************************************
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0
)

#**************************** Schema*****************************************
class Review(TypedDict):
    summary: str
    sentiment: str

structured_model = model.with_structured_output(Review)

#**************************** Input*****************************************
text = """
The hardware is great but the software feels bloated.
There are too many preinstalled apps that I can't remove.
UI looks outdated compared to other brands.
Hoping software updates fix this soon.
"""

response = structured_model.invoke(text)

#**************************** Output*****************************************
print(response)
print(response["summary"])
print(response["sentiment"])
