from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_s', views.create_s, name='create_s'),
    path('edit_s/<int:num>', views.edit_s, name='edit_s'),
    path('delete_s/<int:num>', views.delete_s, name='delete_s'),
]