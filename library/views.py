from django.shortcuts import render
from .forms import UserForm
from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Book


from librarymanagement.settings import EMAIL_HOST_USER


def home_view(request):
   
    return render(request,'library/home.html')


def store(request):
    books = Book.objects.all()
    
    return render(request,'library/store.html', {'books': books})




def login(request):
    
    return render(request,'library/login.html')
def insign(request):
    
    return render(request,'library/insign.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=email, email=email, password=password)
        return redirect('home')
    
    return render(request, 'library/login.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        User.objects.create_user(username=email, email=email, password=password)
        return redirect('home')
    
    return render(request, 'signup.html')
    
    







