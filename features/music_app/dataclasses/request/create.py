from dataclasses import dataclass
from typing import Optional
from datetime import date

@dataclass
class CreateMusicData:
    title: str
    artist: str
    album: Optional[str] =None
    release_date: Optional[date] = None
