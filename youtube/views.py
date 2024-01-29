from django.shortcuts import render
from pytube import *


def youtube(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        video = YouTube(link)
        stream = video.streams.get_lowest_resolution()
        stream.download()
        return render(request, 'index.html')
    return render(request, 'index.html')