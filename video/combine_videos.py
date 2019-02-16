import moviepy.editor as mp

clip1 = mp.VideoFileClip("fan_upside_down.mp4")
clip2 = mp.VideoFileClip("prancercise.mp4")
clip2 = clip2.subclip(10, 13.5)

final_clip = mp.concatenate_videoclips([clip1, clip2])

final_clip.write_videofile("output.mp4")
