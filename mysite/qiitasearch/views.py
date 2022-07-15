from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q
import urllib.request, json, requests
import requests
import json



def index(request):
    p = {
        "page": "1",
        "per_page": "5",
    }
    res = requests.get('https://qiita.com/api/v2/tags/python/items', params=p)
    # print(res.text)
    jsondata = json.loads(res.text)
    print(len(jsondata))

    htmldata=''
    for item in jsondata:
        htmldata = htmldata + item['id'] + '<br>'
        htmldata = htmldata + item['title'] + '<br>'

    # return HttpResponse(res.text)
    return HttpResponse(htmldata)


