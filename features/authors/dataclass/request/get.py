from dataclasses import dataclass

from typing import Optional

@dataclass
class GetAuthorRequest:
    author_id: Optional[int] = None