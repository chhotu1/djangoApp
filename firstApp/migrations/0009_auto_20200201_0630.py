# Generated by Django 3.0.2 on 2020-02-01 01:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0008_auto_20200131_0700'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('email', models.EmailField(blank=True, max_length=100, verbose_name='Email')),
                ('mobile', models.PositiveIntegerField(blank=True, default=0, validators=[django.core.validators.RegexValidator('^\\d+$', 'Only numeric characters are allowed.'), django.core.validators.MaxLengthValidator], verbose_name='Mobile')),
                ('message', models.TextField(blank=True, default='', verbose_name='Message')),
                ('date_added', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.AlterField(
            model_name='signup',
            name='mobile_telephone',
            field=models.PositiveIntegerField(blank=True, default=0, validators=[django.core.validators.RegexValidator('^\\d+$', 'Only numeric characters are allowed.'), django.core.validators.MaxLengthValidator], verbose_name='Mobile'),
        ),
        migrations.AlterField(
            model_name='team',
            name='mobile',
            field=models.PositiveIntegerField(blank=True, default=0, validators=[django.core.validators.RegexValidator('^\\d+$', 'Only numeric characters are allowed.'), django.core.validators.MaxLengthValidator], verbose_name='Mobile'),
        ),
    ]