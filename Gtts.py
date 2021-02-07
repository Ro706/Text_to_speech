from gtts import gTTS
from pyfiglet import Figlet
import os

hour = int(datetime.datetime.now().hour)
if hour >= 0 and hour < 12:
    a = 'Good morning Rohit'
elif hour >= 12 and hour <= 16:
    a = 'Good afternoon Rohit'
else:
    a = 'Good evening Rohit'
output1=gTTS(text=myText,lang=language)
output1.save('wishme.mp3')
os.system("mpv /data/data/com.termux/files/home/wishme.mp3")

#banner
f = Figlet(font = 'slant')
print (f.renderText('Text_to_speech'))
#('Text_to_speech') program
myText = input('enter:')
language = 'en'
output = gTTS(text=myText,lang=language)
output.save('gtts.mp3')
os.system("mpv /data/data/com.termux/files/home/gtts.mp3")
#window user
#os.system('start gtts.mp3')
