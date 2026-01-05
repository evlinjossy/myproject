from dataclasses import dataclass
from typing import Optional

@dataclass
class GetAllAuthorsRequest:
    page_num: int = 1
    limit: int = 10
    search: Optional[str] = None
    sort_by: Optional[str] = None
   
