from gtts import gTTS 

import os 
 
mytext = 'Hello this project is presented by lav, shruti and mukund on text retrieval and text translation with pronounciationnnnn .'
  

myobj = gTTS(text=mytext, slow=False) 
  

myobj.save("output.mp3") 
  
os.system("start output.mp3")