# pip install gTTS
from gtts import gTTS

audio = 'audio.mp3'
language = 'ru'
text = 'Привет. Меня зовут Роман. Я изучаю язык программирования Python'
sp = gTTS(text=text, lang=language, slow=False)

sp.save(audio)
