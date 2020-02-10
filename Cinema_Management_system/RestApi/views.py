from django.shortcuts import render
from django.db import models
from datetime import datetime 
from django.utils import timezone
from django.apps import apps
from Home.models import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

# Create your views here.

def getAlldata(request):
	obj = Movie.objects.all()
	dict_value = {"Movies": list(obj.values("Movie_title","Movie_genre", "Movie_price"))}
	return JsonResponse(dict_value)

def getSpecificData(request):
	obj = Movie.objects.get(pk = pk)
	return JsonResponse({"Movie_title": Movie.Movie_title, "Movie_genre": Movie.Movie_genre, "Movie_price": Movie.Movie_price})

@csrf_exempt
def addApi(request):
	obj =  Movie()
	if request.method == "POST":
		decoded_data = request.body.decode('utf-8')
		obj_data = json.loads(decoded_data)
		obj.Movie_title = obj_data['Movie_title']
		obj.Movie_genre = obj_data['Movie_genre']
		obj.Movie_price = obj_data['Movie_price']
		obj.save()
		return JsonResponse({'message' : "Movie added"})
	else:
		return JsonResponse({'Movie_title':obj.Movie_title,"Movie_genre":obj.Movie_genre ,"Movie_price":obj.Movie_price})


@csrf_exempt
def updateApi(request):
	obj = Movie.object.get(pk = pk)
	if request.method == "PUT":
		decoded_data = request.body.decode('utf-8')
		obj_data = json.loads(decoded_data)
		obj.Movie_title = obj_data['Movie_title']
		obj.Movie_genre = obj_data['Movie_genre']
		obj.Movie_price = obj_data['Movie_price']
		obj.save()
		return JsonResponse({"message" : "Movie Updated"})
	else:
		return JsonResponse({"Movie_title": obj.Movie_title, "Movie_genre": obj.Movie_genre, "Movie_price": obj.Movie_price})


@csrf_exempt
def deleteApi(request, pk = None):
	obj = Movie.objects.get(pk = pk)
	if request.method == 'DELETE':
		obj.delete()
		return JsonResponse({"message": "Sucessfully deleted"})
	else:
		return JsonResponse({"Movie_title" : obj.Movie_title, "Movie_genre":obj.Movie_genre, "Movie_price":obj.Movie_price})


def paginationApi(request, PAGENO):
	SIZE = 3
	skip = SIZE * (PAGENO-1)
	onj = Movie.objects.all()[skip: PAGENO*SIZE]
	dict = {
		"Movies":list(obj.values("Movie_title","Movie_genre", "Movie_price"))}
	return JsonResponse(dict)
	