from dataclasses import dataclass
from datetime import datetime

from board.utils import FromDict


@dataclass
class PostInfo(FromDict):
    user_name: str
    title: str
    content: str
    updated_at: str
