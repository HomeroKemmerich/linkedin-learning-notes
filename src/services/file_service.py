class FileService:

    def __init__(self):
        pass

    def read(path: str) -> str:
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()
    
    def write(path: str, content: str) -> None:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)