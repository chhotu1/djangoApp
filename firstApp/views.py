from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from django.views import View
from .models import SignUp
from django.contrib import messages
def index(request):
    portfolio=Portfolio.objects.all()
    return render(request,'index.html',{'portfolio':portfolio})

class AuthView(View):
    def login(request):
        if request.method == 'POST':
            form = LoginForm()
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                return HttpResponseRedirect('register')
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def register(request):
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                email = form.cleaned_data['email']
                mobile = form.cleaned_data['mobile']
                user = SignUp(username = username,password=password,email=email,mobile_telephone=mobile)
                user.save()
                messages.success(request, f'Account created for {username}!')

                return HttpResponseRedirect('/userHome')
        else:
            form = RegisterForm()
        return render(request, 'register.html', {'form': form})
class AuthUserView(View):
    def userHome(req):
        return render(req,'user/userHome.html')

