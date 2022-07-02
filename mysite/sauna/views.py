from django.shortcuts import render
from django.http import HttpResponse
from .models import Sauna

def index(request):
    data = Sauna.objects.all()
    params = {
        'title': 'Sauna',
        'message': '東京都のサウナ一覧',
        'data': data,
    }
    return render(request, 'sauna/index.html', params)