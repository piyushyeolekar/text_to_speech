from gtts import gTTS 
import os 
  
mytext = 'Hi, I am Piyush'
  
# Language in which you want to convert 
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("welcome.mp3")  
os.system("mpg321 welcome.mp3") 
