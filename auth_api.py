from googleapiclient.discovery import build


class Youtube:
    def __init__(self):
        self.youtube = None
        with open("key.txt", 'r') as f:
            api_key = f.read()
            self.youtube = build('youtube', 'v3', developerKey=api_key)

