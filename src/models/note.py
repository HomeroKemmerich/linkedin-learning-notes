class Note:
    timestamp: str
    url: str
    text: str

    def __init__(self, timestamp: str, url: str, text: str):
        self.timestamp = timestamp
        self.url = url
        self.text = text
    
    def to_dict(self):
        return {
            'timestamp': self.timestamp,
            'url': self.url,
            'text': self.text
        }