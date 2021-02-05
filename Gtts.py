from gtts import gTTS
from pyfiglet import Figlet
import os
#banner
f = Figlet(font = 'slant')
print (f.renderText('Text_to_speech'))
#('Text_to_speech') program
myText = input('enter:')
language = 'en'
output = gTTS(text=myText,lang=language)
output.save('gtts.mp3')
os.system("mpv /data/data/com.termux/files/home")
#window user
#os.system('start gtts.mp3')
