from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'Home'
urlpatterns = [
    path('',views.Index, name = "index"),
    path('uploadmovie/', views.Uploadmovie, name='uploadmovie'),
    path('listmovie/', views.Listmovie, name='list'),
    path('booking/', views.booking, name='book')
    path('booking/save', views.booking_save, name='booking_save')
]