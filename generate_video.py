from gtts import gTTS
from moviepy.editor import *

# STEP 1: Voice Generate
text = """1540 में जन्मा एक शेर, नाम था — महाराणा प्रताप!
राजपुत्र था, पर ठाठ से ज़्यादा मातृभूमि प्यारी थी।
हल्दीघाटी की मिट्टी आज भी उसकी तलवार की गूंज बताती है।
अकबर की बादशाहत को ठुकरा कर, जंगलों में रहा — पर आत्मसम्मान न झुकाया।
घोड़ा चेतक और दिल फौलादी,
ना हार मानी, ना झुका, ना बिका —
1615 में शरीर थमा… पर आत्मा अमर हो गई।
वो गया नहीं — इतिहास में अमर हो गया।
जय मेवाड़! जय महाराणा प्रताप!"""

tts = gTTS(text, lang='hi')
tts.save("voice.mp3")

# STEP 2: Video Generate
clip = ImageClip("image.jpg").set_duration(20)
audio = AudioFileClip("voice.mp3")
clip = clip.set_audio(audio)

clip.write_videofile("maharana_pratap.mp4", fps=24)
