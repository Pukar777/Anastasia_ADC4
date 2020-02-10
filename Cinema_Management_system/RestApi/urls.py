from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "RestApi"

urlpatterns = [
    path('api/',views.getAlldata, name = "alldata"),
    path('api/<int:pk/>',views.getSpecificData, name = "specificdata"),
    path('api/add',views.addApi, name = "updateapi"),
    path('api/update/<int:pk>',views.updateApi,name = "updateapi"),
    path('api/delete/<int:pk>',views.deleteApi ,name = "deleteapi"),
    path('api/page/<int:PAGENO>/', views.paginationApi, name = "api_Photon_pagination"),
]