from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
import urllib.request, json, requests
from .models import Gourmet
from .forms import FindForm


def index(request):
    data = Gourmet.objects.all()
    params = {
        'title': 'gourmet/index',
        'message': 'お店一覧',
        'data': data,
    }
    return render(request, 'gourmet/index.html', params)


def find(request):
    if (request.method == 'POST'):
        msg = 'お店検索結果'
        form = FindForm(request.POST)
        findstr = request.POST['find']
        data = Gourmet.objects.filter(
            Q(name__contains=findstr) | Q(station__contains=findstr) | Q(genre__contains=findstr))
    else:
        msg = 'お店検索'
        form = FindForm()
        data = Gourmet.objects.all()
    params = {
        'title': 'Gourmet',
        'message': msg,
        'form': form,
        'data': data,
    }
    return render(request, 'gourmet/find.html', params)


def download(request):
    data = Gourmet.objects.all()
    params = {
        'title': 'gourmet/download',
        'message': 'お店一覧',
        'data': data,
    }
    return render(request, 'gourmet/download.html', params)


def index2(request):
    str = '<h3>Hello Django.</h3>'
    # url = 'https://webservice.recruit.co.jp/hotpepper/gourmet/v1/?key=76cb152c603e76a8&large_area=Z011&address=%E8%B5%A4%E5%9D%82&format=json'
    url = 'https://webservice.recruit.co.jp/hotpepper/gourmet/v1/'
    payload = {
        "key": "76cb152c603e76a8",
        "large_area": "Z011",
        "address": "赤坂",
        "cocktail": "1",
        "shochu": "1",
        "sake": "1",
        "wine": "1",
        "count": "100",
        "format": "json",
    }
    r = requests.get(url, params=payload)
    jsn = r.json()
    numall = jsn["results"]["results_available"]

    html = f'{numall}<br>'
    num = int(jsn["results"]["results_returned"])
    for i in range(num):
        # shops.append(jsn["results"]["shop"][i]["name"])
        # html = html + jsn["results"]["shop"][i]["name"] + '<br>'
        html = f'{html}' \
               f'{jsn["results"]["shop"][i]["name"]} ／ ' \
               f'{jsn["results"]["shop"][i]["station_name"]} ／ ' \
               f'{jsn["results"]["shop"][i]["genre"]["name"]} ／ ' \
               f'{jsn["results"]["shop"][i]["close"]} ／ ' \
               f'Wi-Fi:{jsn["results"]["shop"][i]["wifi"]} ／ ' \
               f'{jsn["results"]["shop"][i]["urls"]["pc"]}' \
               f'<br>'

    return HttpResponse(html)
    # return HttpResponse(jsn["results"]["shop"][0]["name"])
    # return HttpResponse(int(jsn["results"]["results_returned"])+1)
