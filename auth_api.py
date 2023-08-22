import json

from googleapiclient.discovery import build


class Youtube:
    def __init__(self):
        self.youtube = None
        self.ytoauth2 = None
        with open("key.txt", 'r') as f:
            api_key = f.read()
            self.youtube = build('youtube', 'v3', developerKey=api_key)
        with open("client_secrets.json") as f:
            secrets_dict = json.load(f)
            oauth2_key = secrets_dict['web']['client_id']
            self.ytoauth2 = build('youtube', 'v3', developerKey=oauth2_key)

