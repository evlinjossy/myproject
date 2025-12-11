from dataclasses import dataclass
from typing import Optional
from datetime import date

@dataclass
class UpdateTodoData:
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[date] = None
    is_completed: Optional[bool] = None
