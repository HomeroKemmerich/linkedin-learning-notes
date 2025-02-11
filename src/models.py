from typing import List

class Course:
    title: str
    description: str
    chapters: List[Chapter]

class Chapter:
    title: str
    videos: List[Video]

class Video:
    title: str
    notes: List[Note]

class Note:
    timestamp: str
    text: str