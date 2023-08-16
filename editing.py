import json
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
from unidecode import unidecode

from constants import ILLEGAL_CHARACTERS
from utils import fix_title


def get_title_string(vid):
    s = os.path.basename(vid)
    s = s.removesuffix(".mp4")
    return s

def edit_videos(my_date, vids_and_ids):
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
    outro_text = TextClip("Thanks for watching!", fontsize=50, color="white", font="Impact")
    outro_text = outro_text.set_position(("center", "center"))
    outro_text = outro_text.set_duration(12)

    intro_final = CompositeVideoClip([intro, intro_text]).fx(fadein, 1).fx(fadeout, 1)
    outro_final = CompositeVideoClip([outro, outro_text]).fx(fadein, 1).fx(fadeout, 1)

    vids.append(intro_final)
    i = 1
    for vid in glob(import_path + "/*.mp4"):
        v = VideoFileClip(vid)
        title_string = get_title_string(vid)
        title_string = fix_title(title_string, ILLEGAL_CHARACTERS)
        # Get from file: id
        # 'Hayami Hana'
        vid_id = vids_and_ids[title_string]
        # vid_info = json.load(f"data/{yyyymmdd}/{title_string}.json")
        desc_txt += str(i) + ". https://www.youtube.com/watch?v=" + vid_id + "\n"
        title_text = TextClip(str(i) + ". " + title_string, fontsize=30, color="white", font="Impact")
        title_text = title_text.set_duration(30).set_position(("center", "bottom"))
        r = random.randint(0, math.floor(v.duration) - 30)
        v = v.subclip(r, r + 30)
        v = v.fx(fadein, 1).fx(fadeout, 1)
        v = v.fx(fadein, 1).fx(fadeout, 1)
        v = CompositeVideoClip([v, title_text])
        i += 1
        vids.append(v)

    vids.append(outro_final)
    desc_txt += "\nAuto-generated Highlights taken from YouTube's \"Popular on YouTube\" section"
    with open(f"data/{yyyymmdd}_highlights.txt", 'w') as f:
        f.write(desc_txt)

    final_vid = concatenate_videoclips(vids)
    final_path = "videos/edited/" + yyyymmdd + "_highlights.mp4"
    final_vid.write_videofile(final_path)
    for v in vids:
        v.close()

    return final_path
