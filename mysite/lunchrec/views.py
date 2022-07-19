from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import LunchrecList
from .forms import LunchrecListForm

def index(request):
    data = LunchrecList.objects.all()
    params = {
        'title': 'LunchRec',
        'message': '',
        'data': data,
    }
    return render(request, 'lunchrec/index.html', params)


def create(request):
    if (request.method == 'POST'):
        obj = LunchrecList()
        lunchrecList = LunchrecListForm(request.POST, instance=obj)
        lunchrecList.save()
        return redirect(to='/lunchrec')
    params = {
        'title': 'LunchRec/create',
        'form': LunchrecListForm(),
    }
    return render(request, 'lunchrec/create.html', params)


def edit(request, num):
    obj = LunchrecList.objects.get(id=num)
    if (request.method == 'POST'):
        lunchrecList = LunchrecListForm(request.POST, instance=obj)
        lunchrecList.save()
        return redirect(to='/lunchrec')
    params = {
        'title': 'LunchRec/edit',
        'id': num,
        'form': LunchrecListForm(instance=obj)
    }
    return render(request, 'lunchrec/edit.html', params)


def delete(request, num):
    data = LunchrecList.objects.get(id=num)
    if (request.method == 'POST'):
        data.delete()
        return redirect(to='/lunchrec')
    params = {
        'title': 'LunchRec/delete',
        'id': num,
        'obj': data,
    }
    return render(request, 'lunchrec/delete.html', params)



