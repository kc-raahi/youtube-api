from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx, AudioFileClip, afx
from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip

if __name__ == "__main__":
    uw_vid = "misc/Underwater cam Marchand breaks Phelps 400IM world record at Worlds  NBC Sports.mp4"
    timestamps = [[2, 8], [27, 35], [56, 63], [87, 95], [118, 125], [152, 160], [186, 193], [215, 224], [242, 250]]
    clips = []
    clips_with_fades = []
    for t in timestamps:
        clips.append(VideoFileClip(uw_vid).subclip(t[0], t[1]))
        clips_with_fades.append(VideoFileClip(uw_vid).subclip(t[0], t[1]).fx(vfx.fadein, 1).fx(vfx.fadeout, 1))
    combined = concatenate_videoclips(clips)
    combined_fades = concatenate_videoclips(clips_with_fades)
    t = TextClip("Test Text", fontsize=50, font="Impact", color="white").set_position(("center", "bottom"))
    t = t.set_duration(30)
    combined = CompositeVideoClip([combined, t])
    combined.write_videofile("misc/Start and Turns.mp4")
    # combined_fades.write_videofile("misc/Walls with Fades.mp4")
