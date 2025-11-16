from typing import TypedDict


class Person(TypedDict):
    name: str
    age: int
    isEmployed: bool

new_person: Person = {
    "name": "John Doe",
    "age": 30,
    "isEmployed": True
}
new_person_0: Person = {
    "name": 1100,
    "age": '90',
    "isEmployed": True
}

print(new_person)
print(new_person_0)