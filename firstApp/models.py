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
        verbose_name_plural = "Our Portfolio"
    def __str__(self):
        return self.portfolio


class SignUp(User):
    mobile_telephone = models.PositiveIntegerField('Mobile',default=0,blank=True,max_length=18, validators=[telephone, MaxLengthValidator])
    image = models.ImageField('Image', upload_to='media/user', default='',blank=True)

    def __str__(self):
        return  self.username

