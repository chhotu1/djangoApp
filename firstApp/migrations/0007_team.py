# Generated by Django 3.0.2 on 2020-01-31 01:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0006_auto_20200130_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('email', models.EmailField(blank=True, max_length=100, verbose_name='Email')),
                ('mobile', models.PositiveIntegerField(blank=True, default=0, max_length=18, validators=[django.core.validators.RegexValidator('^\\d+$', 'Only numeric characters are allowed.'), django.core.validators.MaxLengthValidator], verbose_name='Mobile')),
                ('image', models.ImageField(blank=True, default='', upload_to='media/team', verbose_name='Image')),
                ('description', models.CharField(blank=True, default='', max_length=200, verbose_name='Description')),
                ('date_added', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
            },
        ),
    ]
