from django.db import models
from django.contrib.auth.models import User
from django.core.validators import *

telephone = RegexValidator(r'^\d+$', 'Only numeric characters are allowed.')
class Portfolio(models.Model):
    image = models.ImageField('Image',upload_to='media/image',default='')
    description = models.CharField('Description',max_length=200,default='',blank=True)
    date_added = models.DateTimeField(auto_now_add=False,auto_now=True)
    portfolio = models.CharField('Our Portfolio',max_length=256, choices=[('app', 'app'), ('card', 'card'), ('web', 'web')])
    class Meta:
        verbose_name_plural = "Portfolios"
        verbose_name ='Portfolio'
    def __str__(self):
        return self.portfolio


class SignUp(User):
    mobile_telephone = models.PositiveIntegerField('Mobile',default=0,blank=True,max_length=18, validators=[telephone, MaxLengthValidator])
    image = models.ImageField('Image', upload_to='media/user', default='',blank=True)

    def __str__(self):
        return  self.username


class Team(models.Model):
    name = models.CharField('Name',max_length=200)
    email = models.EmailField('Email',max_length=100,blank=True)
    specialization = models.CharField('Specialization',max_length=100,default='',blank=True)
    mobile = models.PositiveIntegerField('Mobile', default=0, blank=True, max_length=18,validators=[telephone, MaxLengthValidator])
    image = models.ImageField('Image',upload_to='media/team',default='',blank=True)
    description = models.TextField('Description',default='',blank=True)
    date_added = models.DateTimeField(auto_now_add=False,auto_now=True)
    class Meta:
        verbose_name_plural = "Teams"
        verbose_name = 'Team'
    def __str__(self):
        return self.email



