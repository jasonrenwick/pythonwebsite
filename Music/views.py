from django.http import HttpResponse
from django.shortcuts import render
import requests
import json


def index(request):
    return HttpResponse("<h1> this is the music app homepage</h1>")


def test(request):
    return HttpResponse("<h2> my second page </h2>")


def profile(request):
    jsonlist = []
    req = requests.get('https://api.github.com/users/jasonrenwick')
    jsonlist.append(json.loads(req.content))
    parseddata = []
    userdata = {}

    for data in jsonlist:
        userdata['name'] = data['name']
        
    content = req.text
    return HttpResponse(content)
