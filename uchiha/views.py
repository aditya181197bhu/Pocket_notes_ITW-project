from django.shortcuts import render
from django.utils import timezone
from .models import *
from django.shortcuts import redirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from .models import Notes4
from django.db import connection
from .forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.


def download(request):                                                                                  #This is our download page view
    cursor = connection.cursor()
    cursor.execute('''SELECT id,title,subject,uploader,created_date,tags,link FROM uchiha_notes4''')
    row = cursor.fetchall()
    return render(request,'uchiha/download.html',{'p':row})

def upload(request):                                                                                    #rhis is our upload page view
    if request.method == 'POST':
        form = UploadForm(request.POST)                                                                 # will redirect it to form.py
        if form.is_valid():
            notes = form.save(commit=False)                                                             # save it later
            #notes.title = request.POST.get('title')
            #notes.tags = request.POST.get('tags')
            #notes.subject = request.POST.get('subject')
            #notes.link = request.POST.get('link')                                                      # manually inputted
            notes.author=request.user
            notes.uploader = request.user
            notes.save()                                                                                 # save the entries
        return render(request, 'uchiha/upload.html',{'form':form})
    else:
        form = UploadForm()
    return render(request, 'uchiha/upload.html',{'form': form})

def getstarted(request):
    return render(request,'uchiha/getstarted.html',{})                                                   #get started page view

def userlogin(request):
    return render(request,'uchiha/userlogin.html')

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)                                          #try to authenticate the user
        login(request, user)
        if next:                                                                                            # check
            return redirect(next)
        return redirect('/home')

    context = {
        'form': form,
    }
    return render(request, "uchiha/login.html", context)


def register_view(request):
    next= request.GET.get('next')
    form = UserRegisterForm( request.POST or None)
    if form.is_valid():
        user = form.save( commit=False )
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/home')

    context={
        'form':form,
    }
    return render(request,"uchiha/register.html",context)

def logout_view(request):
    logout(request)
    return redirect('/')


@login_required
def home(request):
    return render(request,"uchiha/home.html",{})

def upload2(request):
    form=UploadForm()
    if request.method=='post':
        form=UploadForm(request.data)
        if form.is_valid():
            form.save()
            return redirect('')
    return render(request, 'uchiha/upload.html', locals())

def waste(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('text'):
            post = Post()
            post.title = request.POST.get('title')
            post.text = request.POST.get('text')
            post.author_id=1
            post.save()
        return render(request, 'uchiha/post_list.html')
    else:
        return render(request, 'uchiha/post_list.html')

@login_required
def profile(request):
    cursor = connection.cursor()
    a=request.user
    cursor.execute('''SELECT id,title,subject,uploader,created_date,tags,link FROM uchiha_notes4 where uploader=%s''',[a])
    row = cursor.fetchall()
    return render(request, 'uchiha/profile.html', {'p': row})

@login_required
def search(request):
    if request.method =="POST":
        if request.POST.get('search'):
            a=request.POST.get('search')
            cursor = connection.cursor()
            cursor.execute('''SELECT id,title,subject,uploader,created_date,tags,link FROM uchiha_notes4 where uploader=%s OR id=%s OR title=%s OR subject=%s OR created_date=%s OR tags=%s''', [a,a,a,a,a,a])
            row = cursor.fetchall()
            return render(request, 'uchiha/search.html', {'p': row})

    return render(request,'uchiha/search.html',{})

def comm(request):
    pass