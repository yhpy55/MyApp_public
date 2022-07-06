Django3.0.4 Friendモデルを使ってテストアプリを作成する手順
-----
### 1. Djangoプロジェクト(mysite)作成
コンソールを開いて以下のコマンドを入力する。（MyDjangoフォルダが存在しない場合は作成する）
```
cd (MyDocuments)/GitHub/MyDjango
django-admin startproject mysite
cd mysite
python manage.py runserver
```

### 2. runserverの起動確認
以下のURLをブラウザで開き、Djangoのスタートページが表示されることを確認する。
```
http://localhost:8000/
```
-----
### 3. Djangoアプリケーション作成
```
python manage.py startapp hello
```
### [hello/views.py] 編集
```
from django.http import HttpResponse
def index(request):
   return HttpResponse("Hello Django.")
```
### 4. [mysite/urls.py] 編集
```
import hello.views as hello

urlpatterns = [
    （中略）
    path('hello/', hello.index),
]
```
### 5. [mysite/settings.py] 編集
```
INSTALLED_APPS = [
    （中略）
    'hello',
]
```

### 6. 動作確認：Hello Django.
以下のURLをブラウザで開き、Hello Django. が表示されることを確認する。
```
http://localhost:8000/
```
-----
### 7. [hello/models.py] 作成
```
from django.db import models

class Friend(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=200)
    gender = models.BooleanField()
    age = models.IntegerField(default=0)
    birthday = models.DateField()

    def __str__(self):
        return f'<Friend:id= {str(self.id)}, {self.name} ({str(self.age)})>'
```

### 8. makemigrations/migrate
```
$ python manage.py makemigrations hello
$ python manage.py migrate
```

### 9. createsuperuser
```
$ python manage.py createsuperuser
Username (leave blank to use 'django'): admin
Email address: django@mysite.com
Password: 
Password (again): 
```

### 10. [hello/admin.py] 編集
```
from django.contrib import admin
from .models import Friend

admin.site.register(Friend)
```

### 11. 動作確認：[Django administration]画面
以下のURLをブラウザで開き、[Django administration]画面が表示されることを確認する。
```
http://localhost:8000/admin/
```
-----
### 12. テストユーザ追加  
[Django administration]画面の右上[add friend +]ボタンより3ユーザくらい追加する。

### 13. [hello/views.py] 編集
```
from django.shortcuts import render
from django.http import HttpResponse
from .models import Friend

def index(request):
    data = Friend.objects.all()
    params = {
        'title': 'Hello',
        'message': 'member list',
        'data': data,
    }
    return render(request, 'hello/index.html', params)
```

### 14. [hello/templates/hello/index.html] 作成
bootstrapリンク：https://getbootstrap.jp/docs/4.3/getting-started/introduction/#css
```
{% load static %}
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{title}}</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" crossorigin="anonymous">
</head>
<body class="container">
    <h1 class="display-4 text-primary">{{title}}</h1>
    <p class="h5 mt-4">{{message|safe}}</p>
    <table class="table">
        <tr>
            <th>ID</th>
            <th>NAME</th>
            <th>GENDER</th>
            <th>MAIL</th>
            <th>AGE</th>
            <th>BIRTHDAY</th>
        </tr>
    {% for item in data %}
        <tr>
            <td>{{item.id}}</td>
            <td>{{item.name}}</td>
            <td>{% if item.gender == False %}male{% endif %}
                {% if item.gender == True %}female{% endif %}</td>
            <td>{{item.mail}}</td>
            <td>{{item.age}}</td>
            <td>{{item.birthday}}</td>
        </tr>
    {% endfor %}
    </table>
</body>
</html>
```

### 15. [hello/urls.py] 編集
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

### 16. 動作確認：テストアプリ
以下のURLをブラウザで開き、登録したユーザがリスト表示されることを確認する。
```
http://localhost:8000/hello/
```

以上。ユーザ一覧表示アプリの動作確認まで

---

ユーザ一覧表示アプリにcreate, edit, delete画面を追加する
-----
## create画面作成
### 17. [hello/forms.py] 編集
```
from django import forms
from .models import Friend

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name','mail','gender','age','birthday']
```
### 18. [hello/views.py] 編集
```
from django.shortcuts import redirect
from .forms import FriendForm
```
```
def create(request):
    if (request.method == 'POST'):
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title': 'Hello',
        'form': FriendForm(),
    }
    return render(request, 'hello/create.html', params)
```
### 19. [template/hello/create.html] 編集
```
{% load static %}
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>{{title}}</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" crossorigin="anonymous">
</head>
<body class="container">
    <h1 class="display-4 text-primary">{{title}}</h1>
    <form action="{% url 'create' %}" method="post">
        {% csrf_token %}
        <table class="table">
            {{ form.as_table }}
            <tr><th><td>
                <input type="submit" value="click" class="btn btn-primary mt-2">
            </td></th></tr>
        </table>
    </form>
</body>
</html>
```
### 19. [hello/urls.py] 編集
```
urlpatterns = [
    （略）
    path('create', views.create, name='create'),
]
```
### 20. 動作確認：create画面
以下のURLをブラウザで開き、画面が表示されることを確認する。
```
http://localhost:8000/hello/create
```
- テストユーザを追加登録し、一覧画面に遷移することを確認する。
- 一覧画面で追加ユーザが表示されることを確認する。
-----
## edit画面作成
### 21. [hello/views.py] 編集：edit関数
```
def edit(request, num):
    obj = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title': 'Hello',
        'id':num,
        'form': FriendForm(instance=obj)
    }
    return render(request, 'hello/edit.html', params)
```
### 22. [hello/edit.html] 編集：edit画面
```
{% load static %}
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{title}}</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" crossorigin="anonymous">
</head>
<body class="container">
    <h1 class="display-4 text-primary">{{title}}</h1>
    <form action="{% url 'edit' id %}" method="post">
        {% csrf_token %}
        <table class="table">
            {{ form.as_table }}
            <tr><th><td>
                <input type="submit" value="click" class="btn btn-primary mt-2">
            </td></th></tr>
        </table>
    </form>
</body>
</html>
```
### 23. [hello/templates/index.html] 編集
```
    {% for item in data %}
        <tr>
    (中略)
            <td><a href="{% url 'edit' item.id %}">Edit</a></td>
        </tr>
    {% endfor %}
```
### 24. [hello/urls.py] 編集
```
urlpatterns = [

    path('edit/<int:num>', views.create, name='edit'),
]
```
-----
## delete画面作成
### 21. [hello/views.py] 編集：delete関数
```
def delete(request, num):
    friend = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend.delete()
        return redirect(to='/hello')
    params = {
        'title': 'Hello',
        'id':num,
        'obj': friend,
    }
    return render(request, 'hello/delete.html', params)
```
### 22. [hello/edit.html] 編集：delete画面
```
{% load static %}
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{title}}</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" crossorigin="anonymous">
</head>
<body class="container">
    <h1 class="display-4 text-primary">{{title}}</h1>
    <p>※以下のレコードを削除します。</p>
    <table class="table">
        <tr><th>name</th><td>{{obj.id}}</td></tr>
        <tr><th>address</th><td>{{obj.address}}</td></tr>
        <tr><th>fee</th><td>{{obj.fee}}</td></tr>
        <tr><th>holiday</th><td>{{obj.holiday}}</td></tr>
    </table>
    <form action="{% url 'delete' id %}" method="post">
        {% csrf_token %}
            <tr><th><td>
                <input type="submit" value="click" class="btn btn-primary">
            </td></th></tr>
    </form>
</body>
</html>
```
### 23. [hello/templates/index.html] 編集
```
    {% for item in data %}
        <tr>
    (中略)
            <td><a href="{% url 'edit' item.id %}">Edit</a></td>
            <td><a href="{% url 'delete' item.id %}">Delete</a></td>
        </tr>
    {% endfor %}
```
### 24. [hello/urls.py] 編集
```
urlpatterns = [
    (中略)
    path('edit/<int:num>', views.create, name='edit'),
    path('delete/<int:num>', views.delete, name='delete'),
]
```
-----
### 25. [hello/views.py] 編集：ジェネリックビュー
```
from django.views.generic import ListView
from django.views.generic import DetailView
```
```
class FriendList(ListView):
    model = Friend

class FriendDetail(DetailView):
    model = Friend
```
### 26. [hello/urls.py] 編集：ジェネリックビュー
```
from .views import FriendList, FriendDetail
```
```
urlpatterns = [

    path('list', FriendList.as_view()),
    path('detail/<int:pk>', FriendDetail.as_view()),
]
```
### 27. [templates/hello/friend_list.html] 編集：ジェネリックビュー
```
{% load static %}
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>{{title}}</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" crossorigin="anonymous">
</head>
<body class="container">
    <h1 class="display-4 text-primary">Friends List</h1>
    <table class="table">
        <tr>
            <th>id</th>
            <th>name</th>
            <th></th>
        </tr>
        {% for item in object_list %}
        <tr>
            <th>{{item.id}}</th>
            <td>{{item.name}}</td>
            <td><a href="/hello/detail/{{item.id}}">detail</a></td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
```
### 28. [hello/templates/friend_detail.html] 編集：ジェネリックビュー
```
{% load static %}
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>{{title}}</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" crossorigin="anonymous">
</head>
<body class="container">
    <h1 class="display-4 text-primary">Friends List</h1>
    <table class="table">
        <tr>
            <th>id</th>
            <th>{{object.id}}</th>
        </tr>
        <tr>
            <th>name</th>
            <td>{{object.name}}</td>
        </tr>
        <tr>
          <th>mail</th>
          <td>{{object.mail}}</td>
        </tr>
        <tr>
          <th>gender</th>
          <td>{{object.gender}}</td>
        </tr>
        <tr>
          <th>age</th>
          <td>{{object.age}}</td>
        </tr>
    </table>
</body>
</html>
```
-----
### 29. [hello/templates/hello/find.html] 編集：find画面
```
{% load static %}
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{title}}</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" crossorigin="anonymous">
</head>
<body class="container">
    <h1 class="display-4 text-primary">{{title}}</h1>
    <p>{{message|safe}}</p>
    <form action="{% url 'find' %}" method="post">
        {% csrf_token %}
        {{ form.as_table }}
        <tr><th></th><td>
            <input type="submit" value="click" class="btn btn-primary mt-2"></td></tr>
        </form>
        <hr>
        <table>
            <tr>
                <th>id</th>
                <th>name</th>
                <th>mail</th>
            </tr>
            {%for item in data %}
            <tr>
                <th>{{item.id}}</th>
                <td>{{item.name}}({{item.age}})</td>
                <td>{{item.mail}}</td>
            </tr>
            {% endfor %}
        </table>
</body>
</html>
```
### 30. [hello/views.py] 編集：find画面
```
from .forms import FindForm
```
```
def find(request):
    if (request.method == 'POST'):
        form = FindForm(request.POST)
        find = request.POST['find']
        data = Friend.objects.filter(name=find)
        msg = 'Result: ' + str(data.count())
    else:
        msg = 'search words...'
        form = FindForm()
        data = Friend.objects.all()
    params = {
        'title': 'Hello',
        'message': msg,
        'form': form,
        'data': data,
    }
    return render(request, 'hello/find.html', params)
```
### 31. [hello/forms.py] 編集：find画面
```
class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
```
### 32. [hello/urls.py] 編集：find画面
```
urlpatterns = [

    path('find', views.find, name='find'),
]
```
