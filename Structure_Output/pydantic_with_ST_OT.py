from pydantic import BaseModel,EmailStr,Field
from typing import List, Optional
# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv

# load_dotenv()

# model=ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')


class Student(BaseModel):
    name: str
    age: int
    email: EmailStr=Field(description="Email of the student")
    cgpa: float=Field(description="CGPA of the student",gt=0,lt=4,default=0.0)
    
    
    


new_student= {'name': 'John Doe','email':'john.doe@example.com','age':25}


student=Student(**new_student)
student_dict=student.model_dump()
student_json=student.model_dump_json()

print(student_dict)
print(student_json)
