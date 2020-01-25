from django.shortcuts import render, redirect
from .models import Customer
from .models import MovieRequest
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.db.models import Q
from .forms import OurForm

# Create your views here.


def Index(request):
	return render(request=request, template_name='Customer/index.html')


def Signup(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		if(password1==password2):
			if User.objects.filter(username=username).exists():
				messages.info(request,'Username taken')
				return redirect('/signup')
			elif User.objects.filter(email=email).exists():
				messages.info(request,'Email taken')
				return redirect('/signup')
			else:
				user = User.objects.create_user(username=username,password=password1, email=email, first_name=first_name,last_name=last_name)
				user.save();
				return redirect('/login')
		else:
			messages.info(request,'Password is not matching.')
			return redirect('/signup')
		return redirect('/')
	else:
		return render(request=request, template_name='Customer/Signup.html')


def Login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)
			return redirect("/")
		else:
			messages.info(request,'invalid credentials')
			return redirect('/login')
	else:
		return render(request=request, template_name='Customer/login.html')

def Logout(request):
	auth.logout(request)
	return redirect('/')

def RequestMovie(request):
	if request.method == "POST":
		form = OurForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('Customer:list')
	else:
		form = OurForm()
	return render(request, "Customer/upload.html", {"form": form})

def List_movies(request):

    query = ""
    context = {}
    if request.GET:
        query = request.GET['q']
    movie = get_data_queryset(query)
    context['movies'] = movie
    return render(request, "Customer/movie_list.html", context)

def get_data_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        movies = MovieRequest.objects.filter(
            Q(title__icontains=q)
        )

        for MovieRequest in movies:
            queryset.append(movie)

    return (set(queryset))

def Delete_movie(request, pk=None):
    movie = MovieRequest.objects.get(pk=pk)
    movie.delete()
    return redirect('/requestedmovie')