import math
import os
import random
from glob import glob

from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.compositing.concatenate import concatenate_videoclips
from moviepy.video.fx.fadein import fadein
from moviepy.video.fx.fadeout import fadeout
from moviepy.video.io.VideoFileClip import VideoFileClip

from constants import CLIP_LENGTH


def get_title_and_channel(vid, vid_dicts, import_path):
    vid_id = vid.removesuffix('.mp4')
    vid_id = vid_id.removeprefix(import_path)
    vid_id = vid_id.replace('\\', '').replace('/', '')
    for v in vid_dicts:
        if v['id'] == vid_id:
            return os.path.basename(v['snippet']['title']), os.path.basename(v['snippet']['channelTitle'])
    return None


def get_views(vid_dicts, vid_id):
    for vid in vid_dicts:
        if vid['id'] == vid_id:
            return vid['statistics']['viewCount']
    return None


def edit_videos(my_date, vids_and_ids, vid_dicts):
    yyyymmdd = my_date.strftime("%Y%m%d")
    nicedate = my_date.strftime("%B %d, %Y")
    import_path = "videos/raw/" + yyyymmdd
    vids = []
    desc_txt = "These highlights contain the following videos:\n\n"
    intro = VideoFileClip("videos/bookends/raw intro.mp4")
    outro = VideoFileClip("videos/bookends/raw outro.mp4")

    intro_text = TextClip("Popular on YouTube Highlights: " + nicedate, fontsize=50, color="white", font="Impact")
    intro_text = intro_text.set_position(("center", "center"))
    intro_text = intro_text.set_duration(13)

    intro_subtext = TextClip("Daily selection of clips taken from \"Popular on YouTube\"",
                          fontsize=40, color="white", font="Impact")
    intro_subtext = intro_subtext.set_position(("center", "bottom")).set_duration(13)
    outro_text = TextClip("Thanks for watching!", fontsize=50, color="white", font="Impact")
    outro_text = outro_text.set_position(("center", "center"))
    outro_text = outro_text.set_duration(12)

    intro_final = CompositeVideoClip([intro, intro_text, intro_subtext]).fx(fadein, 1).fx(fadeout, 1)
    outro_final = CompositeVideoClip([outro, outro_text]).fx(fadein, 1).fx(fadeout, 1)

    vids.append(intro_final)
    i = 1
    for vid in glob(import_path + "/*.mp4"):
        v = VideoFileClip(vid)
        vlen = CLIP_LENGTH if v.duration > CLIP_LENGTH else v.duration
        title_string, chname = get_title_and_channel(vid, vid_dicts, import_path)
        # title_string = fix_title(title_string, ILLEGAL_CHARACTERS)
        vid_id = vid.removesuffix('.mp4').removeprefix(import_path).replace('\\', '').replace('/', '')
        views = get_views(vid_dicts, vid_id)
        # vid_info = json.load(f"data/{yyyymmdd}/{title_string}.json")
        desc_txt += str(i) + ". https://www.youtube.com/watch?v=" + vid_id + "\n"
        title_text = TextClip(str(i) + ". " + title_string, fontsize=20, color="white", font="Impact")
        title_text = title_text.set_duration(vlen).set_position(("center", "bottom"))
        channel_text = TextClip("Channel: " + chname, fontsize=30, color="white", font="Impact")
        channel_text = channel_text.set_duration(vlen).set_position(("left", "top"))
        view_text = TextClip(views + " views", fontsize=30, color="white", font="Impact")
        view_text = view_text.set_duration(vlen).set_position(("right", "top"))
        r = 0 if vlen <= CLIP_LENGTH else random.randint(0, math.floor(v.duration) - vlen)
        v = v.subclip(r, r + vlen)
        v = v.fx(fadein, 1).fx(fadeout, 1)
        v = v.fx(fadein, 1).fx(fadeout, 1)
        v = CompositeVideoClip([v, title_text, channel_text, view_text])
        i += 1
        vids.append(v)

    vids.append(outro_final)
    desc_txt += "\nAuto-generated Highlights taken from YouTube's \"Popular on YouTube\" section"
    with open(f"data/{yyyymmdd}_highlights.txt", 'w') as f:
        f.write(desc_txt)

    final_vid = concatenate_videoclips(vids, method="compose")
    final_path = "videos/edited/" + yyyymmdd + "_highlights.mp4"
    final_vid.write_videofile(final_path)
    for v in vids:
        v.close()

    return final_path
