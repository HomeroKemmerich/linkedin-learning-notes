from typing import List
from models.video import Video

class Chapter:
    title: str
    videos: List[Video]

    def __init__(self, title: str, videos: List[Video]):
        self.title = title
        self.videos = videos

    def to_dict(self):
        return {
            'title': self.title,
            'videos': [video.to_dict() for video in self.videos]
        }