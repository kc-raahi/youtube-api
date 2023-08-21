import random

import pytube.exceptions
from constants import NUM_OF_VIDEOS, ILLEGAL_CHARACTERS
from misc.download_test import download_video
from utils import fix_title


def select_video_to_download(vids_to_dl, url_storage, vid_dicts):
    while True:
        vid = random.choice(vids_to_dl)
        if not url_storage.already_used(vid):
            return vid


def download_videos(vids_to_dl, url_storage, datestr, by_url, vid_dicts):
    # used_videos = set()
    path = "videos/raw/" + datestr
    dl_ct = NUM_OF_VIDEOS
    # f = open(filename, 'a')
    while dl_ct > 0:
        vid = select_video_to_download(vids_to_dl, url_storage, vid_dicts)
        title = fix_title(by_url[vid], ILLEGAL_CHARACTERS) + '.mp4'
        try:
            download_video(vid, vid_dicts, path, title)
            dl_ct -= 1
            # used_videos.add(vid)
            url_storage.add_used_url(vid)
            vids_to_dl.remove(vid)
        except pytube.exceptions.AgeRestrictedError:
            print(f"Not using {vid} because of age restriction")
