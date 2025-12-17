from dataclasses import dataclass
from typing import Optional
from datetime import date

@dataclass
class CreateTodoData:
    title: str
    description: Optional[str] = ""
    due_date: Optional[date] = None
    is_completed: Optional[bool] = False
