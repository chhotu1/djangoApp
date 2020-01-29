from django import forms
class LoginForm(forms.Form):
    email=forms.CharField(label='Email',max_length=20,required=True,
    widget=forms.TextInput(attrs={'class':'form-control inputsize','placeholder':'email','type':'email'}))
    password = forms.CharField(label='Password',required=True, max_length=30,
    widget=forms.TextInput(attrs={'class': 'form-control inputsize','placeholder': 'password','type':'password'}))

class RegisterForm(forms.Form):
    name=forms.CharField(label='Name',max_length=30,required=True,
    widget=forms.TextInput(attrs={'class':'form-control inputsize','type':'text','placeholder':'name'}))
    mobile = forms.CharField(label='Mobile',max_length=30, required=True,
    widget=forms.TextInput(attrs={'class': 'form-control inputsize', 'type': 'text','placeholder':'uid'}))
    email=forms.CharField(label='Email',max_length=20,required=True,
    widget=forms.TextInput(attrs={'class':'form-control inputsize','placeholder':'email','type':'email'}))
    password = forms.CharField(label='Password',required=True, max_length=30,
    widget=forms.TextInput(attrs={'class': 'form-control inputsize','placeholder': 'password','type':'password'}))



