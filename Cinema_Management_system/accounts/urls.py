from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'Account'

urlpatterns = [
    path('login/', views.Login, name='login'),

    path('signup/', views.Signup, name='signup'),

   	path('logout/', views.Logout, name='logout'),
]