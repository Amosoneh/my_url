from django.shortcuts import render, redirect
from django.http import HttpResponse
# from rest_framework.response import Response,redirect
# from rest_framework.decorators import api_view
from .models import UrlShortener
# from .serializers import UrlShortenerSerializer

import random, string
from .forms import Url


# Create your views here.


# @api_view(['POST'])
# def shortenUrl(request):
#     data = request.data
#     s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1'
#     shorturl = ("".join(random.sample(s, 5)))
#     UrlShortener.objects.create(
#         longurl=data['longurl'],
#         shorturl=shorturl
#     )
#     longurl = data['longurl']
#     shorturl = 'http://localhost:8000' + shorturl


# context = {
#     'longurl': longurl,
#     'shorturl': shorturl
# }
# return redirect('/')


# def redirectUrl(request, shorturl):
#     try:
#         obj = UrlShortener.objects.get(shorturl=shorturl)
#     except UrlShortener.DoesNotExist:
#         obj = None
#     if obj is not None:
#         return redirect(obj.longurl)

def urlShort(request):
    if request.method == 'POST':
        # form = UrlShortener(request.POST)
        shorturl = ''.join(random.choice(string.ascii_letters)
                           for x in range(5))
        short = 'http://localhost:8000/' + shorturl
        longurl = request.POST['link']
        new_url = UrlShortener(longurl=longurl, shorturl=short)
        new_url.save()
        return render(request, 'index.html', context={'shorturl': short})
    # else:
    # form = Url()
    data = UrlShortener()
    context = {
        # 'form': form,
        'data': data
    }
    return render(request, 'index.html', context)


def urlRedirect(request, pk):
    try:
        data = UrlShortener.objects.get(shorturl=pk)
    except UrlShortener.DoesNotExist:
        return redirect('/')

    if data is not None:
        print(data.longurl)
        return redirect('https://' + data.longurl)


def index(request):
    return render(request, 'index.html')
