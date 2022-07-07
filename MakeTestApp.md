Django3.0.4 TestAppアプリ作成手順
-
-----
### 0. 前提条件
- Python 3.10.x
- Django 3.0.4
- Django project名：MyDjango
- Django app名：TestApp
- 作業用ディレクトリ：(???)/GitHub/MyDjango
 (例)C:\Users\0502_Python\Documents\GitHub\MyDjango
- 使用ツール：VSCode or PyCharm
-----
### 1-1. Djangoプロジェクト(MyDjango)作成
- (???)\GitHub\MyDjangoフォルダを開く（存在しない場合は作成する）
```
cd (???)/GitHub/MyDjango
```
- コンソールを開いて以下のコマンドを入力する。
```
django-admin startproject MyDjango
cd MyDjango
python manage.py runserver 8000
```

### 1-2. runserverの実行と起動確認
- コンソールを開いて以下のコマンドを入力する。
```
python manage.py runserver 8000
```
- ブラウザで以下のURLを開き、Djangoのスタートページ(ロケット離陸)が表示されることを確認する。
```
http://localhost:8000/
```
-----
### 1-3. TestAppアプリの作成(startapp)
```
python manage.py startapp TestApp
```
### 1-4. [TestApp/views.py] 編集
```
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   return HttpResponse("Django! TestApp.")
```
### 1-5. [MyDjango/urls.py] 編集
```
from django.contrib import admin
from django.urls import path
import TestApp.views as TestApp

urlpatterns = [
    （中略）
    path('TestApp/', TestApp.index),
]
```
### 1-6. [MyDjango/settings.py] 編集
```
INSTALLED_APPS = [
    （中略）
    'TestApp',
]
```

### 1-7. 動作確認：TestApp Django.
- ブラウザで以下のURLを開き、Django! TestApp. が表示されることを確認する。
```
http://localhost:8000/
```
-----
### 2-1. [TestApp/models.py] 作成
```
from django.db import models

class MyList(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=200)
    gender = models.BooleanField()
    age = models.IntegerField(default=0)
    birthday = models.DateField()

    def __str__(self):
        return f'<MyList:id= {str(self.id)}, {self.name} ({str(self.age)})>'
```

### 2-2. makemigrations/migrate 実行
```
$ python manage.py makemigrations TestApp
$ python manage.py migrate
```

### 2-3. createsuperuser 実行
- 以下のコマンドを実行する。
```
$ python manage.py createsuperuser
```
- 管理用ユーザ名、メールアドレス、パスワードを入力する。
```
Username (leave blank to use 'django'): admin
Email address: admin@mydjango.com
Password: ****************
Password (again): ****************
```

### 2-4. [TestApp/admin.py] 編集
```
from django.contrib import admin
from .models import MyList

admin.site.register(MyList)
```

### 2-5. 動作確認：[Django administration]画面
ブラウザで以下のURLを開き、[Django administration]画面が表示されることを確認する。
```
http://localhost:8000/admin/
```
-----
### 3-1. テストユーザ追加  
- [Django administration]画面を表示する。
- 画面の右上[add MyList +]ボタンより3ユーザくらい追加する。

### 3-2. [TestApp/views.py] 編集
```
from django.shortcuts import render
from django.http import HttpResponse
from .models import MyList

def index(request):
    data = MyList.objects.all()
    params = {
        'title': 'TestApp',
        'message': 'メンバー一覧',
        'data': data,
    }
    return render(request, 'TestApp/index.html', params)
```

### 3-3. [TestApp/templates/TestApp/index.html] 作成
- (参考)bootstrapリンク：https://getbootstrap.jp/docs/4.3/getting-started/introduction/#css
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

### 3-4. [TestApp/urls.py] 編集
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

### 3-5. 動作確認：テストアプリ
- ブラウザで以下のURLを開き、登録したユーザがリスト表示されることを確認する。
```
http://localhost:8000/TestApp/
```

- 以上でTestAppのユーザ一覧表示の動作確認が完了となる。

---

ユーザ一覧表示アプリにcreate, edit, delete画面を追加する
-----
## 4-1. create画面作成
### 17. [TestApp/forms.py] 編集
```
from django import forms
from .models import MyList

class MyListForm(forms.ModelForm):
    class Meta:
        model = MyList
        fields = ['name','mail','gender','age','birthday']
```
### 18. [TestApp/views.py] 編集
```
from django.shortcuts import redirect
from .forms import MyListForm
```
```
def create(request):
    if (request.method == 'POST'):
        obj = MyList()
        MyList = MyListForm(request.POST, instance=obj)
        MyList.save()
        return redirect(to='/TestApp')
    params = {
        'title': 'TestApp',
        'form': MyListForm(),
    }
    return render(request, 'TestApp/create.html', params)
```
### 19. [template/TestApp/create.html] 編集
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
### 19. [TestApp/urls.py] 編集
```
urlpatterns = [
    （略）
    path('create', views.create, name='create'),
]
```
### 20. 動作確認：create画面
以下のURLをブラウザで開き、画面が表示されることを確認する。
```
http://localhost:8000/TestApp/create
```
- テストユーザを追加登録し、一覧画面に遷移することを確認する。
- 一覧画面で追加ユーザが表示されることを確認する。
-----
## edit画面作成
### 21. [TestApp/views.py] 編集：edit関数
```
def edit(request, num):
    obj = MyList.objects.get(id=num)
    if (request.method == 'POST'):
        MyList = MyListForm(request.POST, instance=obj)
        MyList.save()
        return redirect(to='/TestApp')
    params = {
        'title': 'TestApp',
        'id':num,
        'form': MyListForm(instance=obj)
    }
    return render(request, 'TestApp/edit.html', params)
```
### 22. [TestApp/edit.html] 編集：edit画面
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
### 23. [TestApp/templates/index.html] 編集
```
    {% for item in data %}
        <tr>
    (中略)
            <td><a href="{% url 'edit' item.id %}">Edit</a></td>
        </tr>
    {% endfor %}
```
### 24. [TestApp/urls.py] 編集
```
urlpatterns = [

    path('edit/<int:num>', views.create, name='edit'),
]
```
-----
## delete画面作成
### 21. [TestApp/views.py] 編集：delete関数
```
def delete(request, num):
    MyList = MyList.objects.get(id=num)
    if (request.method == 'POST'):
        MyList.delete()
        return redirect(to='/TestApp')
    params = {
        'title': 'TestApp',
        'id':num,
        'obj': MyList,
    }
    return render(request, 'TestApp/delete.html', params)
```
### 22. [TestApp/edit.html] 編集：delete画面
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
### 23. [TestApp/templates/index.html] 編集
```
    {% for item in data %}
        <tr>
    (中略)
            <td><a href="{% url 'edit' item.id %}">Edit</a></td>
            <td><a href="{% url 'delete' item.id %}">Delete</a></td>
        </tr>
    {% endfor %}
```
### 24. [TestApp/urls.py] 編集
```
urlpatterns = [
    (中略)
    path('edit/<int:num>', views.create, name='edit'),
    path('delete/<int:num>', views.delete, name='delete'),
]
```
-----
### 25. [TestApp/views.py] 編集：ジェネリックビュー
```
from django.views.generic import ListView
from django.views.generic import DetailView
```
```
class MyListList(ListView):
    model = MyList

class MyListDetail(DetailView):
    model = MyList
```
### 26. [TestApp/urls.py] 編集：ジェネリックビュー
```
from .views import MyListList, MyListDetail
```
```
urlpatterns = [

    path('list', MyListList.as_view()),
    path('detail/<int:pk>', MyListDetail.as_view()),
]
```
### 27. [templates/TestApp/MyList_list.html] 編集：ジェネリックビュー
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
    <h1 class="display-4 text-primary">MyLists List</h1>
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
            <td><a href="/TestApp/detail/{{item.id}}">detail</a></td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
```
### 28. [TestApp/templates/MyList_detail.html] 編集：ジェネリックビュー
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
    <h1 class="display-4 text-primary">MyLists List</h1>
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
### 29. [TestApp/templates/TestApp/find.html] 編集：find画面
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
### 30. [TestApp/views.py] 編集：find画面
```
from .forms import FindForm
```
```
def find(request):
    if (request.method == 'POST'):
        form = FindForm(request.POST)
        find = request.POST['find']
        data = MyList.objects.filter(name=find)
        msg = 'Result: ' + str(data.count())
    else:
        msg = 'search words...'
        form = FindForm()
        data = MyList.objects.all()
    params = {
        'title': 'TestApp',
        'message': msg,
        'form': form,
        'data': data,
    }
    return render(request, 'TestApp/find.html', params)
```
### 31. [TestApp/forms.py] 編集：find画面
```
class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
```
### 32. [TestApp/urls.py] 編集：find画面
```
urlpatterns = [

    path('find', views.find, name='find'),
]
```
