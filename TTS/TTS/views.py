from django.http import HttpResponse
from django.shortcuts import render
import os 
from gtts import gTTS 
from playsound import playsound

def home(request):
    return render(request,'index.html')

def speech(request):
    mytext = request.POST.get('text','')
    if(mytext==''):
        mytext='No text to Speak'
    tts = gTTS(text=mytext, lang='en', slow=False) 
    tts.save("sound.mp3") 
    playsound('sound.mp3')
    return render(request,'afterSpeech.html')