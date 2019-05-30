from django.urls import path

# from same directory import views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]