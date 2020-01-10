from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('form/', views.form, name='form')
]