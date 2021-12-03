from dataclasses import dataclass


@dataclass
class PostInfo:
    user_name: str
    title: str
    content: str