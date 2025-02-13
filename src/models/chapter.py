from typing import List
from models.video import Video

class Chapter:
    title: str
    videos: List[Video]

    def __init__(self, title: str):
        self.title = title

    def to_dict(self):
        return {
            'title': self.title,
            'videos': [video.to_dict() for video in self.videos]
        }
    
    def get_videos(self):
        return self.videos
    
    def set_videos(self, videos):
        self.videos = videos
        return self