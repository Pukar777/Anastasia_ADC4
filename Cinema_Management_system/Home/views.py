from django.shortcuts import render, redirect
from .forms import OurForm
from .models import Movie
from django.db.models import Q
from django.views.generic import ListView
# Create your views here.


def Index(request):
	objects = Movie.objects.all()
	return render(request, 'index.html', {'objects':objects})

def Uploadmovie(request):
    if request.method == "POST":
        form = OurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = OurForm()

    return render(request, "upload.html", {"form": form})

def Listmovie(request):

    query = ""
    context = {}
    if request.GET:
        query = request.GET['q']
    movie = get_data_queryset(query)
    context['movies'] = movie
    return render(request, "listmovie.html", context)


def get_data_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        movies = Movie.objects.filter(Q(Movie_title__icontains=q))

        for movie in movies:
            queryset.append(movie)

    return (set(queryset))


def booking(request)
    return render(request, 'booking.html')