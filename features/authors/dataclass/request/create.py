from dataclasses import dataclass

@dataclass
class AuthorRequest:
    name: str
    age:int
    language:str
    country:str