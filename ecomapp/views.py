from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth   
from django.contrib import messages

from ecomapp.models import Product

# Create your views here.

def welcome_page(request):
    return render(request,'home.html')

def login_page(request):
    return render(request,'login.html')

def signup_page(request):
    return render(request,'signup.html')

def mobile_page(request):
    return render(request,'mobiles.html')

def fashion_page(request):
    return render(request,'Fashion.html')

def userpage(request):
    return render(request,'user.html')  


def usercreate(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email']

        if password==cpassword:  
            if User.objects.filter(username=username).exists(): 
                messages.info(request, 'This username already exists!!!!!!')
                return redirect('signup_page')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email)
                user.save()

                
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')            
            return redirect('signup_page')   
        return redirect('login_page')
    else:
        return render(request,'signup.html')


def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			messages.info(request, f'welcome {username}')
			return redirect('userpage')
		else:
			messages.info(request, 'Invalid Username or Password. Try Again.')
			return redirect('login_page')
	else:
		
		return redirect('login_page')

def logout(request):
	auth.logout(request)
	return redirect('welcome_page')

