
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from Note import models
from .models import Note
from django.contrib.auth import authenticate, login, logout

def base(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email= request.POST.get('uemail')
        password = request.POST.get('upassword')
        newUser = User.objects.create_user(username=name, email=email, password=password)
        newUser.save()
        return redirect('/loginn')
    return render(request, 'register.html')




def loginn(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('upassword')
        userr = authenticate(request, username=name, password=password)
        if userr is not None:
            login(request, userr)
            return redirect('/home')
        else:
            return redirect('/login')

    return render(request, 'login.html')




def home(request):
    context = {
        'posts': Note.objects.all()
    }
    return render(request, 'home.html', context)



def newNote(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        nnote = models.Note(title=title, description=description, author=request.user)
        nnote.save()
        return redirect('/home')
    
    return render(request, 'Add.html')




def myNote(request):
    context = {
        'notes': Note.objects.filter(author= request.user)
    }
    return render(request, 'blog.html', context)



def signout(request):
    logout(request)
    return redirect('/loginn')
