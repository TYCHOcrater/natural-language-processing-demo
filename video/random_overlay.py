import random
import moviepy.editor as mp

video = mp.VideoFileClip("dance.mp4")

video_duration = video.duration
clip_duration = 1.5

clips = []

for i in range(0,10):
    start = random.uniform(0, video_duration - clip_duration)
    end = start + clip_duration

    clip = video.subclip(start,end)
    clip = clip.set_position((random.randint(-100, 800), random.randint(-100, 400)))
    clip = clip.set_start( i / 2.0)

    clips.append(clip)

final_clip = mp.CompositeVideoClip(clips)

final_clip.wirte_videofile("random_dance.mp4")
