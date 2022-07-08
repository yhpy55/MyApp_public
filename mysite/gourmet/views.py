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
        msg = '飲み屋検索結果'
        form = FindForm(request.POST)
        findstr = request.POST['find']
        data = Gourmet.objects.filter(
            Q(name__contains=findstr) | Q(station__contains=findstr) | Q(genre__contains=findstr))
    else:
        msg = '飲み屋検索'
        form = FindForm()
        data = Gourmet.objects.all()
    params = {
        'title': 'Gourmet',
        'message': msg,
        'form': form,
        'data': data,
    }
    return render(request, 'gourmet/find.html', params)


def download2(request):
    data = Gourmet.objects.all()
    params = {
        'title': 'gourmet/download',
        'message': 'お店一覧',
        'data': data,
    }
    return render(request, 'gourmet/download.html', params)

def download(request):
    if (request.method == 'POST'):
        msg = '飲み屋検索'
        form = FindForm()
        data = Gourmet.objects.all()
        # msg = '飲み屋検索結果'
        # form = FindForm(request.POST)
        # findstr = request.POST['find']
        # data = Gourmet.objects.filter(
        #     Q(name__contains=findstr) | Q(station__contains=findstr) | Q(genre__contains=findstr))
    else:
        msg = '飲み屋検索'
        form = FindForm()
        data = Gourmet.objects.all()
    params = {
        'title': 'Gourmet',
        'message': msg,
        'form': form,
        'data': data,
    }

    webapi_url = 'https://webservice.recruit.co.jp/hotpepper/gourmet/v1/'
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
    r = requests.get(webapi_url, params=payload)
    jsn = r.json()

    num = int(jsn["results"]["results_returned"])
    for i in range(num):
        s_name = jsn["results"]["shop"][i]["name"]
        s_station = jsn["results"]["shop"][i]["station_name"]
        s_genre = jsn["results"]["shop"][i]["genre"]["name"]
        s_holiday = jsn["results"]["shop"][i]["close"]
        s_wifi = jsn["results"]["shop"][i]["wifi"]
        s_non_smoking = jsn["results"]["shop"][i]["non_smoking"]
        s_urls = jsn["results"]["shop"][i]["urls"]["pc"]
        s_coupon_urls = jsn["results"]["shop"][i]["coupon_urls"]["pc"]

        g = Gourmet.objects.create(name = f"{s_name}",
                                   station = f"{s_station}",
                                   genre = f"{s_genre}",
                                   holiday = f"{s_holiday}",
                                   wifi = f"{s_wifi}",
                                   non_smoking = f"{s_non_smoking}",
                                   urls = f"{s_urls}",
                                   coupon_urls = f"{s_coupon_urls}")

    return render(request, 'gourmet/find.html', params)


def viewdata(request):
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

    num = int(jsn["results"]["results_returned"])
    html = f'ヒット件数：{num}<br>'
    html = f'{html}総ヒット件数：{numall}<br>'
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
