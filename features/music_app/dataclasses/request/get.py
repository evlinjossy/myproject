from dataclasses import dataclass
from typing import Optional

@dataclass
class GetMusicData:
    music_id: Optional[int] = None
