from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .forms import *
from .models import *
def index(request):
    portfolio=Portfolio.objects.all()
    return render(request,'index.html',{'portfolio':portfolio})

def login(request):
    loginForm = LoginForm()
    return render(request,'login.html',{'loginForm':loginForm})
def register(request):
    form=RegisterForm()
    return render(request,'register.html',{'form':form})

def about(request):
    return render(request,'about.html')
