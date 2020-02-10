from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from Home.models import Customer

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
				obj = Customer(Customer_Firstname = first_name, Customer_Lastname = last_name, Customer_Username = username, Customer_email = email)
				obj.save();

				return redirect('/login')
		else:
			messages.info(request,'Password is not matching.')
			return redirect('/signup')
		return redirect('/')
	else:
		return render(request=request, template_name='Signup.html')

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
		return render(request=request, template_name='login.html')
def Logout(request):
	auth.logout(request)
	return redirect('/')