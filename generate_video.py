from gtts import gTTS
from moviepy.editor import ImageClip, AudioFileClip, CompositeVideoClip

# 1. टेक्स्ट इनपुट
text = "Welcome to our AI generated video!"

# 2. Text to Speech
tts = gTTS(text)
tts.save("audio.mp3")

# 3. Image से वीडियो बनाओ
image_path = "background.jpg"  # ध्यान: ये इमेज होनी चाहिए तुम्हारी डायरेक्टरी में
clip = ImageClip(image_path).set_duration(5)  # 5 सेकंड का वीडियो

# 4. ऑडियो को ऐड करो
audio = AudioFileClip("audio.mp3")
video = clip.set_audio(audio)

# 5. वीडियो को सेव करो
video.write_videofile("final_video.mp4", fps=24)
