from typing import List
from models.note import Note

class Video:
    title: str
    notes: List[Note]

    def __init__(self, title: str, notes: List[Note]):
        self.title = title
        self.notes = notes

    def to_dict(self):
        return {
            'title': self.title,
            'notes': [note.to_dict() for note in self.notes]
        }