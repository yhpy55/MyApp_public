from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Sauna
from .forms import SaunaForm

def index(request):
    data = Sauna.objects.all()
    params = {
        'title': 'Sauna',
        'message': '東京都のサウナ一覧',
        'data': data,
    }
    return render(request, 'sauna/index.html', params)

def create(request):
    if (request.method == 'POST'):
        obj = Sauna()
        sauna = SaunaForm(request.POST, instance=obj)
        sauna.save()
        return redirect(to='/sauna')
    params = {
        'title': 'Sauna/create',
        'form': SaunaForm(),
    }
    return render(request, 'sauna/create.html', params)

def edit(request, num):
    obj = Sauna.objects.get(id=num)
    if (request.method == 'POST'):
        sauna = SaunaForm(request.POST, instance=obj)
        sauna.save()
        return redirect(to='/sauna')
    params = {
        'title': 'Sauna/edit',
        'id':num,
        'form': SaunaForm(instance=obj)
    }
    return render(request, 'sauna/edit.html', params)

def delete(request, num):
    sauna = Sauna.objects.get(id=num)
    if (request.method == 'POST'):
        sauna.delete()
        return redirect(to='/sauna')
    params = {
        'title': 'Sauna/delete',
        'id':num,
        'obj': sauna,
    }
    return render(request, 'sauna/delete.html', params)