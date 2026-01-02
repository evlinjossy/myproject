from dataclasses import dataclass
@dataclass
class AuthorUpdateRequest:
    author_id: int
    name: str
    age: int
    language: str
    country: str
   