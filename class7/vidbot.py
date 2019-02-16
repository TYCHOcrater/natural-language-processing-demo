from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import sys 
import argparse

def compose(text, duration=4.0, outname="sunset_words.mp4"):
    start = 108
    end = start + duration
    clip1 = VideoFileClip("sunset.mp4").subclip(start,end).resize( (1920/2, 1080/2) )
    clip2 = TextClip(text, size=clip1.size).set_duration(4)

    composition = CompositeVideoClip( [ clip1, clip2 ] )

    composition.write_videofile(outname)

text = sys.argv[1]

if len(sys.argv) > 2:
    duration = float(sys.argv[2])
else:
    duration = 3

compose(text, duration)
