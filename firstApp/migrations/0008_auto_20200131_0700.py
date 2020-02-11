# Generated by Django 3.0.2 on 2020-01-31 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0007_team'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portfolio',
            options={'verbose_name': 'Portfolio', 'verbose_name_plural': 'Portfolios'},
        ),
        migrations.AddField(
            model_name='team',
            name='specialization',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Specialization'),
        ),
        migrations.AlterField(
            model_name='team',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='Description'),
        ),
    ]