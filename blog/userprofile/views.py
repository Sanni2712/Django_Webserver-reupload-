from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, request
from mysiteblog.models import BlogModel
from django.contrib.auth.models import User
from .forms import profileupdateform, profilebgupdateform
from django.contrib.auth import authenticate, get_user_model, login, logout
import re



def userprofile(request):

    if request.user.is_authenticated == False:
        return redirect('http://127.0.0.1:8000/login')
    if request.user.is_authenticated:
    	return redirect(f'http://127.0.0.1:8000/profile/{request.user.username}')
    if request.method == 'POST':
        logval = request.POST.get('logoutbutton')
        delete = request.POST.get('delete')
        if logval == 'logout':
            logout(request)
        

def isvalidEmail(email):
    pattern = "^\S+@\S+\.\S+$"
    objs = re.search(pattern, email)
    try:
        if objs.string == email:
            return True
    except:
        return False

    m = BlogModel.objects.all().filter(user=request.user.id)        
    return render(request, 'blog/profile.html', {'m':m})

def edituserprofile(request):
    msg = ""
    mmnbm = request.user.id
    if request.user.is_authenticated:
        if request.method == 'POST':
            delacc = request.POST.get('deletebtn1')
            print(delacc)
            password3 = request.POST.get('password3')
            print(password3)
            dlbtn1 = request.POST.get('delbtnh1')
            print(dlbtn1)
            if delacc == 'delacc':
                mmms = request.user.check_password(password3)
                print(mmms)
                if mmms:
                    logout(request)
                    dbnm = User.objects.get(id=mmnbm)
                    dbnm.delete()
                    return redirect('http://127.0.0.1:8000/login')
                if not mmms:
                	msg="The enterd password is not correct"
                	return render(request, 'blog/profileupdate.html' , {'form':form, 'msg':msg})
                    
            username = request.POST.get('Username')
            email = request.POST.get('Email')
            password1 = request.POST.get('password1')
            print(password1, username, email)
            if User.objects.filter(username=username).exists():
                cmbm = User.objects.get(username=username)
            
            	
            cmbm1 = User.objects.filter(username=username)
            if cmbm1.exists() == True and cmbm.id==request.user.id:
                tbm = True
            if cmbm1.exists() == True and cmbm.id != request.user.id:
                tbm = False
                msg="this username is aldready taken"
            if cmbm1.exists() == False:
            	tbm = True

            if isvalidEmail(str(email)) == False:
                msg="the enterd email is invalid"
            if isvalidEmail(str(email)) == True and tbm == True:
                mmms = request.user.check_password(password1)
                print(mmms)
                if mmms:
                    sma = User.objects.get(username=request.user.username)
                    print(sma)
                    sma = request.user
                    sma.username = username
                    sma.email = email
                    sma.save()

            logval = request.POST.get('logoutbutton')
            if logval =="logout":

                logout(request)
            form2 = profilebgupdateform(request.POST, request.FILES, instance=request.user.profile)
            if form2.is_valid():

                form2.save()
            form = profileupdateform(request.POST, request.FILES, instance=request.user.profile)
            if form.is_valid():

                form.save()
        else:
            form = profileupdateform(instance=request.user.profile)
            form2 = profilebgupdateform(instance=request.user.profile)
        return render(request, 'blog/profileupdate.html' , {'form':form, 'msg':msg})

    else:
    	return redirect('http://127.0.0.1:8000/')
        

def otheruser(request, user):

    userx = User(id=request.user.id)
    dm = BlogModel.objects.filter(blog_like__user__in=[userx.id])
    if request.user.username == user:
        userx = User(id=request.user.id)
        print(user, request.user.username)
        m = BlogModel.objects.all().order_by('-created_at').filter(user=request.user.id)   
        dm = BlogModel.objects.all().order_by('-created_at').filter(blog_like__user__in=[userx.id])

        print(dm)     
        return render(request, 'blog/profile.html', {'m':m})
    us = User.objects.get(username=user)
    m = BlogModel.objects.all().order_by('-created_at').filter(user=us.id)
    return render(request, "blog/otheruser.html", {'os':us, 'm':m})


def edituserbg(request):   
    if request.user.is_authenticated:
        
        if request.method == 'POST':
            logval = request.POST.get('logoutbutton')
            if logval =="logout":
                logout(request)

            form = profilebgupdateform(request.POST, request.FILES, instance=request.user.profile)
            if form.is_valid():

                form.save()
        else:
            form = profilebgupdateform(instance=request.user.profile)
        return render(request, 'blog/profilebgupdate.html' , {'form':form})
    else:
        return redirect('http://127.0.0.1:8000/')
def likeview(request, user):
    userx = User(id=request.user.id)
    dm = BlogModel.objects.filter(blog_like__user__in=[userx.id])
    if request.user.username == user:
        userx = User(id=request.user.id)
        print(user, request.user.username)
        m = BlogModel.objects.all().filter(user=request.user.id)   
        dm = BlogModel.objects.filter(blog_like__user__in=[userx.id])

        print(dm)     
        return render(request, 'blog/profile1.html', {'m':dm})
    if request.user.username != user:    
        return redirect(f'http://127.0.0.1:8000/profile/{user}')

def settings(request, user):

    if request.user.is_authenticated:
        return render(request, 'blog/profile1.html')
    if request.user.username != user:    
        return redirect(f'http://127.0.0.1:8000/profile/{user}')
    
