import pprint
import sys
import os
# Get the path of the directory containing p1.py
current_dir = os.path.dirname(os.path.abspath(__file__))
# Get the path of the directory containing p2.py
parent_dir = os.path.join(current_dir, "..")
sys.path.append(parent_dir)

from pytube import YouTube


def download_video(link, vid_dicts, path=None, filename=None):
    youtubeObject = YouTube(link)
    id = link.removeprefix('https://www.youtube.com/watch?v=')
    pprint.pprint(youtubeObject)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(output_path=path, filename=id + '.mp4')
    except:
        print("An error has occurred")
    print("Download is completed successfully")


if __name__ == "__main__":
    url = 'https://www.youtube.com/watch?v=r6gDwwoAuIo'
    download_video(url, "misc")
