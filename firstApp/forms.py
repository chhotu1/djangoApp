from django import forms
from django.forms import ValidationError
from .models import SignUp
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username=forms.CharField(label='username',max_length=20,required=True,
    widget=forms.TextInput(attrs={'class':'form-control inputsize','placeholder':'Username','type':'text'}))
    password = forms.CharField(label='Password',required=True, max_length=30,
    widget=forms.TextInput(attrs={'class': 'form-control inputsize','placeholder': 'password','type':'password'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) > 0:
            raise forms.ValidationError("username is too short")
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 4:
            raise forms.ValidationError("password is too short")
        return password


class RegisterForm(forms.Form):
    username=forms.CharField(label='Username',max_length=60,required=True,
    widget=forms.TextInput(attrs={'class':'form-control inputsize','type':'text','placeholder':'Username'}))
    mobile = forms.CharField(label='Mobile',max_length=10, required=True,min_length=10,
    widget=forms.TextInput(attrs={'class': 'form-control inputsize', 'type': 'number','placeholder':'Mobile'}))
    email=forms.CharField(label='Email',max_length=100,required=True,
    widget=forms.TextInput(attrs={'class':'form-control inputsize','placeholder':'email','type':'email'}))
    password = forms.CharField(label='Password',required=True, max_length=30,
    widget=forms.TextInput(attrs={'class': 'form-control inputsize','placeholder': 'password','type':'password'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 4:
            raise forms.ValidationError("username is too short")
        return username

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username has already existed.")
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 4:
            raise forms.ValidationError("password is too short")
        return password

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@gmail.com'):
            raise ValidationError('Domain of email is not valid')
        return email

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email has already existed.")
        return email

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        if (mobile.isalnum()):
            raise forms.ValidationError("Please enter a valid mobile number")
        return  mobile




