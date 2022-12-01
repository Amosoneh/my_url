import random
import string

from django.shortcuts import render, redirect, get_object_or_404

from .models import UrlShortener


def urlShort(request):
    if request.method == 'POST':
        shorturl = ''.join(random.choice(string.ascii_letters)
                           for x in range(5))
        short = 'http://localhost:8000/' + shorturl
        longurl = request.POST['link']
        new_url = UrlShortener(longurl=longurl, shorturl=short)
        new_url.save()
        return render(request, 'index.html', context={'shorturl': short})
    data = UrlShortener()
    context = {
        'data': data
    }
    return render(request, 'index.html', context)


def urlRedirect(request, pk):
    data = get_object_or_404(UrlShortener, shorturl="http://localhost:8000/" + pk)
    return redirect('https://' + data.longurl)


def index(request):
    return render(request, 'index.html')
