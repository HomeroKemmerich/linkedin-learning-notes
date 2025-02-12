from typing import List
from note import Note

class Video:
    title: str
    notes: List[Note]

    def __init__(self, title: str, notes: List[Note]):
        self.title = title
        self.notes = notes