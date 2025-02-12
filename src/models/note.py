class Note:
    timestamp: str
    url: str
    text: str

    def __init__(self, timestamp: str, url: str, text: str):
        self.timestamp = timestamp
        self.url = url
        self.text = text