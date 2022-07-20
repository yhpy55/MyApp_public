from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_l', views.create_l, name='create_l'),
    path('edit_l/<int:num>', views.edit_l, name='edit_l'),
    path('delete_l/<int:num>', views.delete_l, name='delete_l'),
]