import sys

from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage

target_playlist_id = "PLj-RvYg7WBWcJH-IFEMKp9is9S3Mr24eG"
target_video_id = "17ct960jgHw"

import os

import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

MISSING_CLIENT_SECRETS_MESSAGE = """
WARNING: Please configure OAuth 2.0

To make this sample run you will need to populate the client_secrets.json file
found at:

   %s

with information from the API Console
https://console.cloud.google.com/

For more information about the client_secrets.json file format, please visit:
https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
"""

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secrets.json"

    # Get credentials and create an API client
    flow = flow_from_clientsecrets(client_secrets_file,
                                   scope=scopes,
                                   message=MISSING_CLIENT_SECRETS_MESSAGE)

    storage = Storage("%s-oauth2.json" % sys.argv[0])
    credentials = storage.get()

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.playlistItems().insert(
        part="snippet",
        body={
          "snippet": {
            "playlistId": target_playlist_id,
            "position": 0,
            "resourceId": {
              "kind": "youtube#video",
              "videoId": target_video_id
            }
          }
        }
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()