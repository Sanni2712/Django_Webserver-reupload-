from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from mysiteblog.models import BlogModel, Likes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model, login, logout
from .forms import PageForm, commentForm
from django.contrib.auth.hashers import check_password


def index(request):
    if request.method == 'POST':
        logval = request.POST.get('logoutbutton')
        if len(logval):
            logout(request)
    return redirect('/blog/blogs')

   
def create(request):
    form = PageForm 
    if request.user.is_authenticated is not True:
        return redirect('/login')

    if request.method == 'POST':
        logval = request.POST.get('logoutbutton')
        if logval == 'logout':
            logout(request)
        msg = ""
        form = PageForm(request.POST, request.FILES)

        if form.is_valid():
            title = request.POST.get('title')
            description =request.POST.get('description')
            category =request.POST.get('category')
            print(category)
            if len(title) and len(description) and len(category): 
                form.title =title
                post = form.save(commit=False)
                post.title=title
                post.description =description
                if category == "</> Coding":
                    post.category = category
                if category == "</> Python":
                    post.category = category
                if category == "</> Java":
                    post.category = category
                if category == "</> C++":
                    post.category = category
                if category == "</> C":
                    post.category = category
                if category == "</> C#":
                    post.category = category
                if category == "Travel":
                    post.category = category
                if category == "Cooking":
                    post.category = category
                if category == "Education": 
                    post.category = category
                if category == "Stories":   
                    post.category = category
                if category == "Memes":   
                    post.category = category    
                print(form)
                post.save()
                request.user.blogmodel.add(post)
                form = PageForm
                pid = post.id
                return redirect(f'/blog/{pid}')
            if not len(title) or len(description):
                msg = "Enter the title"
    return render(request, 'blog/create.html', {'form': form})        


def projects(request):
    logval = request.POST.get('logoutbutton')
    if request.method =='POST':

        if logval == 'logout':
            logout(request)

    m = BlogModel.objects.all().order_by('-created_at')


    return render(request, 'blog/projects.html', {'m': m})

def blogview(request, id):
    form2 = commentForm(request.POST, request.FILES)
    ls = BlogModel.objects.get(id=id)
    mmbs = Likes.objects.all().filter(blogmodel=ls)
    sm = mmbs.count()
    if Likes.objects.all().filter(user=request.user, blogmodel=ls).exists():
        mb = "y"

    if Likes.objects.all().filter(user=request.user, blogmodel=ls).exists() == False:
        mb = "n"
    if request.method == 'POST':
        logval = request.POST.get('logoutbutton')
        like = request.POST.get('likebtn')
        
            
        if logval == 'logout':
            logout(request)
        if like == "liked":
            if request.user.is_authenticated:
                
                if Likes.objects.all().filter(user=request.user, blogmodel=ls).exists():
                    pmb = Likes.objects.all().filter(user=request.user, blogmodel=ls).first()
                    pmb.delete()
                    mb = "n"
                    mmbs = Likes.objects.all().filter(blogmodel=ls)
                    sm = mmbs.count()
                else:
                    like = Likes(user=request.user, blogmodel = ls)
                    like.save()

                    mb = "y"
                    bs = Likes.objects.all().filter(blogmodel=ls)
                    sm = mmbs.count()
                    print(sm)
                if request.method == 'POST':
                    form2 = commentForm(request.POST, request.FILES)

                    if form2.is_valid():
                        comment = form2.save(commit=False)
                        comment.save()
            if request.user.is_authenticated is not True:

                return redirect('/login')        
    return render(request, "blog/blogview.html", {"ls":ls, 'sm':sm, 'mb':mb, 'form':form2})

def search(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        m = BlogModel.objects.all().filter(title__icontains=search) | BlogModel.objects.all().filter(category__icontains=search)
        return render(request, 'blog/projects.html', {'m': m})

    else:
        return redirect('http://127.0.0.1:8000/blog/blogs')

def updateview(request, id):
    post1 = BlogModel.objects.get(id=id)
    qm= request.user
    if request.method == 'POST':
        delete =request.POST.get('deletebutton')
        logval = request.POST.get('logoutbutton')
        savebtn = request.POST.get('savebtn')
        if logval == 'logout':
            logout(request)
        if delete == "delete":
            post1 = BlogModel.objects.get(id=id)
            post1.delete()    
            return redirect('http://127.0.0.1:8000/profile')
    print(request.user)
    print(post1.user)
    if post1.user == qm:
        form = PageForm(request.POST, request.FILES)
        if request.method != 'POST':

            form = PageForm(instance=post1)

        else:
            title = request.POST.get('title')
            description =request.POST.get('description')
            category =request.POST.get('category')
            delete =request.POST.get('deletebutton')
            savebtn = request.POST.get('savebtn')
            print(delete)
            if delete == "delete":
                post1 = BlogModel.objects.get(id=id)
                post1.delete()
                return redirect('http://127.0.0.1:8000/blog/blogs')
            print(category)
            if savebtn == 'save':

                form = PageForm(instance=post1, data=request.POST) 
                post = form.save(commit=False)
                if len(title) and len(description) and len(category): 
                        form.title =title
                        post = form.save(commit=False)
                        post.title=title
                        post.description =description
                        if category == "</> Coding":
                            post.category = category
                        if category == "</> Python":
                            post.category = category
                        if category == "</> Java":
                            post.category = category
                        if category == "</> C++":
                            post.category = category
                        if category == "</> C ":
                            post.category = category
                        if category == "</> C#":
                            post.category = category
                        if category == "Travel":
                            post.category = category
                        if category == "Cooking":
                            post.category = category
                        if category == "Education": 
                            post.category = category
                        if category == "Stories":   
                            post.category = category

                        if category == "Memes":   
                            post.category = category    
                        print(form)
                        post.save()
                        pid = post.id
                        return redirect(f'/blog/{pid}')
                        
        return render(request, "blog/editblog.html", {"form":form, 'postinst':post1})

    else:
        pid = post1.id
        return redirect(f'/blog/{pid}')


