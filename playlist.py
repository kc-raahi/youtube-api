from googleapiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.tools import run_flow, argparser
import googleapiclient.errors

from oauth2client.file import Storage

# Use the file storage
store = Storage("credentials.json")


def add_to_playlist(playlist_id, video_id):
    # Set up OAuth2 flow from client secrets
    flow = flow_from_clientsecrets("client_secrets.json",
                                   scope="https://www.googleapis.com/auth/youtube.force-ssl",
                                   redirect_uri="urn:ietf:wg:oauth:2.0:oob")

    # Run the OAuth2 flow
    credentials = run_flow(flow, store, flags=None)

    # Build the YouTube service
    youtube = build("youtube", "v3", credentials=credentials)

    try:
        request = youtube.playlistItems().insert(
            part="snippet",
            body={
                "snippet": {
                    "playlistId": playlist_id,
                    "position": 0,
                    "resourceId": {
                        "kind": "youtube#video",
                        "videoId": video_id,
                    },
                },
            },
        )
        response = request.execute()

        print(response)
    except googleapiclient.errors.HttpError as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    argparser.add_argument("--vidId", required=True, help="ID of the video to add")
    argparser.add_argument("--playlistId", required=True, help="ID of the playlist")

    args = argparser.parse_args()
    add_to_playlist(args.playlistId, args.vidId)
