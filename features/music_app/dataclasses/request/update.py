from dataclasses import dataclass
from typing import Optional
from datetime import date

@dataclass
class UpdateMusicData:
    music_id:int
    title: Optional[str] = None
    artist: Optional[str] = None
    album: Optional[str] = None
    release_date: Optional[date] = None
