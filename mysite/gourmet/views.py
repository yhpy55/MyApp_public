from django.shortcuts import render
from django.http import HttpResponse
import urllib.request,json,requests

def index(request):
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
   # return HttpResponse(num_all)

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
