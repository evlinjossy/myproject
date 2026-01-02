from dataclasses import dataclass
from typing import Optional
from datetime import date

@dataclass
class CreateMusicData:
    title: str
    author_name: str
    album: Optional[str] =None
    release_date: Optional[date] = None
