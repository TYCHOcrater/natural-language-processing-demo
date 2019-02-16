import random
import moviepy.editor as mp

video = mp.VideoFileClip("dance.mp4")

video_duration = video.duration

clip_duration = 0.5

clips = []

for i in range(0,10):
    start = random.uniform(0, video_duration - clip_duration)

    end = start + clip_duration

    clips.append(video.subclip(start,end))

final_clip = mp.concatenate_videoclips(clips)
final_clip.write_videofile("random_dance.mp4")

