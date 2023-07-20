from django.http import HttpResponse
from django.shortcuts import render
import pyttsx3

def home(request):
    # speak = pyttsx3.init()
    if(request.method=='POST'):
        word=request.POST.get('Word','default')
    #     # print(word)
    #     speak.say(word)
    #     speak.runAndWait()
        param={'word':word}
        return render(request, 'home.html',param)
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')
