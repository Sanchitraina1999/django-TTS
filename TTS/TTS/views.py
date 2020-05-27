from django.http import HttpResponse
from django.shortcuts import render
import os 
from gtts import gTTS 
from playsound import playsound

def home(request):
    return render(request,'index.html')

def speech(request):
    mytext = request.POST.get('text','')
    print(mytext)
    language = 'en'
    tts = gTTS(text=mytext, lang=language, slow=False) 
    tts.save("welcome.mp3") 
    playsound('welcome.mp3')
    return render(request,'speech.html')