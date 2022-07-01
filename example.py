from pyttsx3 import *
from transliterate import* 

while True:
    text=input(">")
    s=print(translit(text, 'en'))
    speak(s)



