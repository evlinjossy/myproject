from dataclasses import dataclass
from typing import Optional

@dataclass
class GetAllAuthorsRequest:
    page: int = 1
    page_size: int = 10
    search: Optional[str] = None
    sort_by: Optional[str] = None
