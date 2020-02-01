from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .forms import LoginForm,RegisterForm,ContactForm
from django.views import View
from .models import SignUp,Team,Portfolio,Contact
from django.contrib import auth
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password
def index(request):
    portfolio=Portfolio.objects.all()
    team = Team.objects.all()
    return render(request,'index.html',{'portfolio':portfolio,'team':team})

def contact(requset):
    if requset.method == 'POST':
        form =ContactForm(requset.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            message = form.cleaned_data['message']
            # send_mail('subject', 'body of the message', 'uic.17mca8058@gmail.com',['chhotukumarsow@gmail.com', 'chhotukumarsow@gmail.com'])
            con = Contact(name=name,email=email,mobile=mobile,message=message)
            con.save();
            messages.success(requset, 'Send Message Successfully')
            return HttpResponseRedirect('contact')
    else:
        form = ContactForm()
    return render(requset,'contact.html',{'form':form})


class AuthView(View):
    def login(request):
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                try:
                    user_v = auth.authenticate(username=username, password=password)
                    if user_v is not None:
                        auth.login(request, user_v)
                        return HttpResponseRedirect('userHome')
                    else:
                        messages.error(request, 'username and password does not exit')
                except auth.ObjectNotExist:
                    print("invalid")
                # return HttpResponse("Hello, world. You're at the polls index.")
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
                user = SignUp(username = username,password=make_password(password),email=email,mobile_telephone=mobile)
                user.save()
                messages.success(request, f'Account created for {username}!')

                return HttpResponseRedirect('/userHome')
        else:
            form = RegisterForm()
        return render(request, 'register.html', {'form': form})
class AuthUserView(View):
    def userHome(req):
        return render(req,'user/userHome.html')

