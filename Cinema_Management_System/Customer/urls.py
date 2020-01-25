from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'Customer'
urlpatterns = [
    path('',views.Index, name = "index"),

   
    path('login/', views.Login, name='login'),


    path('signup/', views.Signup, name='signup'),

   	path('logout/', views.Logout, name='logout'),

   	path('requestmovie/', views.RequestMovie, name='requestmovie'),

   	path('requestedmovie/', views.List_movies, name="list"),

   	path('Movierequest/<int:pk>/', views.Delete_movie, name="delete_movie")
]