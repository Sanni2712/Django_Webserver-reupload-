from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, request
from .models import BlogModel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model, login, logout
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def index(request):
    if request.method == 'POST':
        logval = request.POST.get('logoutbutton')
        if len(logval):
            logout(request)
    return redirect('/home')

def home(request):
    if request.method == 'POST':
        logval = request.POST.get('logoutbutton')
        if len(logval):
            logout(request)
    return render(request, 'blog/home.html')
    

def sign_up(request):
    if request.user.is_authenticated:
        return redirect('http://127.0.0.1:8000/')
    regex1 = "#(\w+)"
    msg = " "
    emailvalidity = False
    usernamevalidity = False
    if request.method == 'POST':
         
        username = request.POST.get('Username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if (re.fullmatch(regex, email)):

            emailvalidity = True
        if len(username) < 3:
            msg = "Username should be atleast 4 characters"
        if emailvalidity == False:
            msg = "Please enter a valid email"
        if len(password1) <= 3: 
            msg = "Password should be atleast 4 characters"
        if password1 != password2:
            msg = "Passwords do not match"
        
        
        try:
            mb = username.split("#")
            ssdfd = mb[1]
            print(ssdfd)
            kks = True
            
        except:
            kks = False
        if kks:
            msg = "Username should not contain any #"  
        if ' ' in username:
            msg = "Username should not contain any spaces"    
        elif kks == False:

            if User.objects.filter(username=username).exists() == True:
                msg="this username is aldready taken"
            else:    

                user = User.objects.create_user(username, email, password1)
                user = authenticate(username=username, password=password1)
                if user is not None:

                    login(request,user=user)
                    return redirect('/profile')
                mms = User.objects.filter(username = username).first()
                
    return render(request, 'blog/register.html', {'msg':msg})

#def dashboard(request):
 #   username4 = None
  #  if request.user.is_authenticated:
      #  username4 = request.user.username
        
   # else:
    #	username4 = "please login"
        
    
    #return render(request, 'main/dashboard.html', {'username':username4})
  
   # user1 = None
   # if request.user.is_authenticated():
    #    user1 = request.user.username


def sign_in(request):
    if request.user.is_authenticated:
        return redirect('http://127.0.0.1:8000/')

    msg2 = " "
    if request.method == 'POST':
        logval = request.POST.get('logoutbutton')
       
        username = request.POST.get('Username')
        password3 = request.POST.get('password1')
        user = authenticate(username=username, password=password3)
        print("user- ", user)
        if user is not None:
            login(request, user)
            return redirect('http://127.0.0.1:8000/')
      
        	#return redirect('http://127.0.0.1:8000/dashboard')
        else:
            msg2="username or password is invalid" 	

    return render(request, 'blog/login.html', {'msg2':msg2})


