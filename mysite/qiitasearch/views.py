from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q
import urllib.request, json, requests
import requests
import json
from .models import QiitaSearch



def index(request):
    webapi_url = 'https://qiita.com/api/v2/items'
    # webapi_urls = 'https://qiita.com/api/v2/tags'
    token = "6f542c4a493bf49d49e08d75d5e3dbfebb9cc2d0"
    headers = {
        'Content-Type': 'application/json',
        'Charset': 'utf-8',
        'Authorization': 'Bearer ' + token
    }
    htmldata = ''
    params = {
        "page": "1",
        "per_page": "100",
        "query": "tag:Python tag:Django title:webアプリ stock:>1",
        "sort": "stock",
    }
    res = requests.get(webapi_url, params=params, headers=headers)
    # res = requests.get(f'{webapi_urls}:Python/items', params=params, headers=headers)
    jsondata = json.loads(res.text)
    for item in jsondata:
        htmldata = htmldata + str(item['likes_count']) + item['title'] + '<br>'
        htmldata = htmldata + str(item['tags']) + '<br>'

    # return HttpResponse(res.text)
    return HttpResponse(htmldata)

def download(request):
    webapi_url = 'https://qiita.com/api/v2/items'
    token = "6f542c4a493bf49d49e08d75d5e3dbfebb9cc2d0"
    headers = {
        'Content-Type': 'application/json',
        'Charset': 'utf-8',
        'Authorization': 'Bearer ' + token
    }
    htmldata = ''
    params = {
        "page": "3",
        "per_page": "100",
        # "query": "tag:Python tag:Django title:webアプリ stock:>1",
        "query": "tag:Python stock:>1",
        # "sort": "stock",
    }
    res = requests.get(webapi_url, params=params, headers=headers)
    # res = requests.get(f'{webapi_urls}:Python/items', params=params, headers=headers)
    jsondata = json.loads(res.text)
    for item in jsondata:
        try:
            g = QiitaSearch.objects.get(qid=item['id'])
        except:
            c = QiitaSearch.objects.create(qid=item['id'],
                                           title=item['title'],
                                           url=item['url'],
                                           created_at=item['created_at'],
                                           updated_at=item['updated_at'],
                                           # comments_count=item['comments_count'],
                                           # reactions_count=item['reactions_count'],
                                           likes_count=item['likes_count'],
                                           # page_views_count=['page_views_count'],
                                         )

    # return HttpResponse(res.text)
    return HttpResponse(htmldata)

def downloada(address):
    # webapi_url = 'https://qiita.com/api/v2/tags/python/items'
    webapi_url = 'https://qiita.com/api/v2/items'
    token = "6f542c4a493bf49d49e08d75d5e3dbfebb9cc2d0"
    headers = {
        "Authorization": "Bearer " + token
    }
    params = {
        "page": "1",
        "per_page": "5",
    }
    res = requests.get(webapi_url, params=params, headers=headers)

    # print(res.text)
    jsondata = json.loads(res.text)
    payload = {
        "key": "76cb152c603e76a8",
        "large_area": "Z011",
        "address": address,
        "cocktail": "1",
        "shochu": "1",
        "sake": "1",
        "wine": "1",
        "count": "100",
        "format": "json",
    }
    r = requests.get(webapi_url, params=payload)
    jsn = r.json()

    return jsn


def write_jsondata(jsn):
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
        shop_id = jsn["results"]["shop"][i]["id"]

        try:
            g = Gourmet.objects.get(shop_id=f"{shop_id}")
        except:
            c = Gourmet.objects.create(name=f"{s_name}",
                                       station=f"{s_station}",
                                       genre=f"{s_genre}",
                                       holiday=f"{s_holiday}",
                                       wifi=f"{s_wifi}",
                                       non_smoking=f"{s_non_smoking}",
                                       urls=f"{s_urls}",
                                       coupon_urls=f"{s_coupon_urls}",
                                       shop_id=f"{shop_id}", )

    return render(request, 'gourmet/find.html', params)



