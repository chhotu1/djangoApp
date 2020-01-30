from django import forms
class LoginForm(forms.Form):
    email=forms.CharField(label='Email',max_length=20,required=True,
    widget=forms.TextInput(attrs={'class':'form-control inputsize','placeholder':'email','type':'email'}))
    password = forms.CharField(label='Password',required=True, max_length=30,
    widget=forms.TextInput(attrs={'class': 'form-control inputsize','placeholder': 'password','type':'password'}))

class RegisterForm(forms.Form):
    username=forms.CharField(label='Username',max_length=60,required=True,
    widget=forms.TextInput(attrs={'class':'form-control inputsize','type':'text','placeholder':'Username'}))
    mobile = forms.CharField(label='Mobile',max_length=10, required=True,min_length=10,
    widget=forms.TextInput(attrs={'class': 'form-control inputsize', 'type': 'number','placeholder':'Mobile'}))
    email=forms.CharField(label='Email',max_length=100,required=True,
    widget=forms.TextInput(attrs={'class':'form-control inputsize','placeholder':'email','type':'email'}))
    password = forms.CharField(label='Password',required=True, max_length=30,
    widget=forms.TextInput(attrs={'class': 'form-control inputsize','placeholder': 'password','type':'password'}))



