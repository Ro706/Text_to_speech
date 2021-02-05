from gtts import gTTS
from pyfiglet import Figlet
import os
#banner
f = Figlet(font = 'slant')
print (f.renderText('Text_to_speech'))
#('Text_to_speech') program
myText = 'hello my name is Ro706 nice to meet u and this is my first text to speech conversion program by using python.'
language = 'en'
output = gTTS(text=myText,lang=language)
output.save('gtts.mp3')
os.system("mpv /data/data/com.termux/files/home/project")
#window user
#os.system('start gtts.mp3')
