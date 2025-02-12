from typing import List
from video import Video

class Chapter:
    title: str
    videos: List[Video]

    def __init__(self, title: str, videos: List[Video]):
        self.title = title
        self.videos = videos