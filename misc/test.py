from googleapiclient.discovery import build
import pandas
import seaborn
import pprint

from auth_api import Youtube

# api_key = 'AIzaSyDI2EHOZnOuLbxT0RYBQ-vQX5-RMLD-oI0'
channel_id = 'UCTkXRDQl0luXxVQrRQvWS6w'

# youtube = build('youtube', 'v3', developerKey=api_key)
youtube = Youtube()

def get_channel_stats(youtube, channel_id):
    request = youtube.channels().list(part='snippet,contentDetails,statistics', id=channel_id)
    response = request.execute()
    return response


if __name__ == "__main__":
    pprint.pprint(get_channel_stats(youtube.youtube, channel_id))
