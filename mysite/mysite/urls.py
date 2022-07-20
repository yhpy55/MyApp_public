"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import top.views as top
import hello.views as hello
import hello1.views as hello1
import gourmet.views as gourmet
import sauna.views as sauna
import qiitasearch.views as qiitasearch
import lunchrec.views as lunchrec
import dev.views as dev

urlpatterns = [
    path('', top.index),
    path('top/', top.index),
    path('admin/', admin.site.urls),
    path('gourmet/', include('gourmet.urls')),
    path('sauna/', include('sauna.urls')),
    path('lunchrec/', include('lunchrec.urls')),
    path('qiitasearch/', include('qiitasearch.urls')),
    path('dev/', include('dev.urls')),
    path('hello/', hello.index),
    path('hello1/', hello1.index),
    # path('gourmet', gourmet.index),
    # path('sauna/', sauna.index),
    # path('dev/', dev.index),
]
