from django.shortcuts import render
from django.http import HttpResponse

from .models import Customer
# Create your views here.

def home(request):
	return render(request=request, template_name='main/home.html',context={"Customer":Customer.objects.all})

def form(request):
	return render(request=request, template_name='main/form.html', context={"form": form})