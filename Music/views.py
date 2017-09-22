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
    req = requests.get('https://api.github.com/users/jonathanchan1')
    jsonlist.append(json.loads(req.content))
    parseddata = []
    userdata = {}

    for data in jsonlist:
        userdata['name'] = data['name']
        userdata['email'] = data['email']
        userdata['public_gists'] = data['public_gists']
        userdata['public_repos'] = data['public_repos']
        userdata['avatar_url'] = data['avatar_url']
        userdata['followers'] = data['followers']
        userdata['following'] = data['following']

    parseddata.append(userdata)
    return HttpResponse(parseddata)
