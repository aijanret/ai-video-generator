from moviepy.editor import *
from gtts import gTTS

# Read the script
with open("script.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Generate audio from text
tts = gTTS(text, lang='hi')
tts.save("audio.mp3")

# Create a background clip (black screen)
clip = ColorClip(size=(1280, 720), color=(0, 0, 0), duration=10)
clip = clip.set_audio(AudioFileClip("audio.mp3"))

# Export final video
clip.write_videofile("output_video.mp4", fps=24)
