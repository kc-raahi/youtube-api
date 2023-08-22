import json
import pprint
import sys
import os
import urllib

# Get the path of the directory containing p1.py
current_dir = os.path.dirname(os.path.abspath(__file__))
# Get the path of the directory containing p2.py
parent_dir = os.path.join(current_dir, "..")
sys.path.append(parent_dir)

from auth_api import Youtube

channel_id = 'UCTkXRDQl0luXxVQrRQvWS6w'

# youtube = build('youtube', 'v3', developerKey=api_key)
youtube = Youtube()


def get_channel_stats(youtube, channel_id):
    request = youtube.channels().list(part='snippet,contentDetails,statistics', id=channel_id)
    response = request.execute()
    return response


def get_popular_videos(youtube):
    request = youtube.videos().list(part='snippet,contentDetails,statistics', chart='mostPopular',
                                    maxResults=50)
    response = request.execute()
    vids = [item for item in response['items']]
    next_page_token = response.get('nextPageToken')
    while next_page_token is not None:
        next_page = youtube.videos().list(part='snippet,contentDetails,statistics', chart='mostPopular',
                                          maxResults=50, pageToken=next_page_token)
        next_response = next_page.execute()
        vids.extend(item for item in next_response['items'])
        next_page_token = next_response.get('nextPageToken')

    return vids


if __name__ == "__main__":
    popular_videos = get_popular_videos(youtube.youtube)
    pprint.pprint(my_channel_videos)


