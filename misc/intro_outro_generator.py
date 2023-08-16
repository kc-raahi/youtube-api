import numpy
from moviepy.video.io.VideoFileClip import VideoFileClip

if __name__ == "__main__":

    start_intro = 31
    end_intro = 44

    start_outro = 48
    end_outro = 60

    vidpath = "misc/Jellyfish Comp.mp4"
    vid = VideoFileClip(vidpath)
    intro = vid.subclip(start_intro, end_intro)
    outro = vid.subclip(start_outro, end_outro)

    intro.write_videofile("bookends/raw intro.mp4")
    outro.write_videofile("bookends/raw outro.mp4")

    # intro_text = TextClip("Popular on YouTube Highlights", fontsize=30, color="white")
    # intro_text = intro_text.set_position(("center", "center"))
    # intro_text = intro_text.set_duration(end_intro - start_intro)
    # outro_text = TextClip("Thanks for watching!", fontsize=30, color="white")
    # outro_text = outro_text.set_position(("center", "center"))
    # outro_text = outro_text.set_duration(end_outro - start_outro)
    #
    # intro_final = CompositeVideoClip([intro, intro_text]).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
    # outro_final = CompositeVideoClip([outro, outro_text]).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
    #
    # intro_final.write_videofile("bookends/intro test.mp4")
    # outro_final.write_videofile("bookends/outro test.mp4")



