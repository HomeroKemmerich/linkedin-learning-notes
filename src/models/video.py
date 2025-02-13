from typing import List
from functions import unformat
from models.note import Note

class Video:
    title: str
    stub: str
    notes: List[Note]

    def __init__(self, title: str):
        self.title = title
        self.stub = unformat(title.lower().replace(' ', '-'))

    def to_dict(self):
        return {
            'title': self.title,
            'notes': [note.to_dict() for note in self.notes]
        }
    
    def get_notes(self):
        return self.notes
    
    def set_notes(self, notes):
        self.notes = notes
        return self