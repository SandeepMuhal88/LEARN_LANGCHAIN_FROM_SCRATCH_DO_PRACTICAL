# from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Literal, Optional, List

load_dotenv()

model = ChatOpenAI(
    model='gpt-3.5-turbo',
    temperature=0
)

# Schema
class Review(TypedDict):
    key_themes: Annotated[List[str], "List of all major themes discussed in the review"]
    summary: Annotated[str, "Short summary of the entire review"]
    sentiment: Annotated[Literal["positive", "negative", "neutral"], "Overall sentiment"]
    pros: Annotated[Optional[List[str]], "All advantages mentioned (list)"]
    cons: Annotated[Optional[List[str]], "All disadvantages mentioned (list)"]
    name: Annotated[str, "Name of the reviewer"]

structured_model = model.with_structured_output(Review)

text = """ 
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Sandeep Muhal
"""

response = structured_model.invoke(text)

print(response)
print(response['key_themes'])
print(response['summary'])
print(response['sentiment'])
print(response['pros'])
print(response['cons'])
print(response['name'])
