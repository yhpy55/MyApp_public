from django.shortcuts import render
from django.http import HttpResponse
import urllib.request, json, requests

def index(request):
    # data = Gourmet.objects.all()
    params = {
        'title': 'top/index',
        'message': 'お店一覧',
        # 'data': data,
    }
    return render(request, 'top/index.html', params)
