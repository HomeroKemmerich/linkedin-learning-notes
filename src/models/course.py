import json

from functions import unformat

from typing import List
from models.chapter import Chapter

from markdown_utilities import md_blocks
from markdown_utilities.pymd import dict_to_md

class Course:
    title: str
    stub: str
    description: str
    chapters: List[Chapter]

    def __init__(self, title: str, description: str):
        self.title = title
        self.stub = unformat(title.lower().replace(':', '').replace(' ', '-'))
        self.description = description
    
    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'chapters': [chapter.to_dict() for chapter in self.get_chapters()]
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=2, ensure_ascii=False)
    
    def to_md(self):
        md_notes = [
            md_blocks.h1(self.title),
            md_blocks.p(self.description),
        ]
        for chapter in self.chapters:
            md_notes.append(md_blocks.h2(chapter.title))
            for video in chapter.videos:
                md_notes.append(md_blocks.h3(video.title))
                for note in video.notes:
                    md_notes.append(md_blocks.h4(f'[{note.timestamp}]({note.url})'))
                    md_notes.append(md_blocks.p(f'{note.text}'))
        return dict_to_md(md_notes)

    def get_chapters(self):
        return self.chapters
    
    def set_chapters(self, chapters):
        self.chapters = chapters
        return self