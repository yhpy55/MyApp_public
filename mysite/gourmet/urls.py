from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('find', views.find, name='find'),
    path('download', views.download, name='download'),
    path('viewdata', views.viewdata, name='viewdata'),
    path('dlakasaka', views.dlakasaka, name='dlakasaka'),
]
