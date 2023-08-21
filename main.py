import random
from datetime import date
import os.path

from auth_api import Youtube
from constants import STORAGE_FILE, ILLEGAL_CHARACTERS
from downloading import download_videos
from editing import edit_videos
from misc.info_test import get_popular_videos
from url_storage import URLStorage
from utils import fix_title


def create_info_file(vid, datestr):
    info_path = f"data/{datestr}"
    title = vid['snippet']['title']
    id = vid['id']
    fullpath = info_path + '/' + id + '.txt'
    if not os.path.exists(info_path):
        os.makedirs(info_path)
    f = open(fullpath, 'w')
    f.write(vid['id'])
    f.close()


def get_popular_urls():
    yt = Youtube()
    popular_video_data = get_popular_videos(yt.youtube)
    urls = []
    by_name = {}
    by_url = {}
    for vid in popular_video_data:
        title = fix_title(vid['snippet']['title'], ILLEGAL_CHARACTERS)
        url = "https://www.youtube.com/watch?v=" + vid['id']
        urls.append(url)
        by_name[title] = vid['id']
        by_url[url] = fix_title(title, ILLEGAL_CHARACTERS)
    return urls, by_name, by_url, popular_video_data


if __name__ == "__main__":
    random.seed(10)

    td = date.today()
    td_str = td.strftime("%Y%m%d")

    url_storage = URLStorage(STORAGE_FILE)
    # Get URLs for "Popular on YouTube"
    popular_urls, vids_and_ids, links_and_titles, vid_dict_list = get_popular_urls()
    # pprint.pprint(vids_and_ids)

    # existing_urls = url_storage.get_existing_urls()

    # with open(url_storage.filename, 'r') as f:
    #     existing_urls = f.read().split("\n")

    # popular_urls, existing_urls = url_storage.add_to_urls(popular_urls, existing_urls)

    # Download
    download_videos(popular_urls, url_storage, td_str, links_and_titles, vid_dict_list)

    daily_vid_path = edit_videos(td, vids_and_ids, vid_dict_list)

    url_storage.close()
