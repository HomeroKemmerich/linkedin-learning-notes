import unicodedata

def unformat(text: str) -> str:
    nfdk = unicodedata.normalize('NFKD', text)
    return nfdk.encode('ascii', 'ignore').decode('utf-8')

def timestamp_to_seconds(timestamp: str) -> int:
    hours, minutes, seconds = timestamp.split(':')
    return int(hours) * 3600 + int(minutes) * 60 + int(seconds)