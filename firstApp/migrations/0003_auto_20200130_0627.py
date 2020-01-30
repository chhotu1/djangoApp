# Generated by Django 3.0.2 on 2020-01-30 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0002_auto_20200129_2319'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portfolio',
            options={'verbose_name_plural': 'Our Portfolio'},
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='file_type',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='text_field',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='description',
            field=models.CharField(default='', max_length=200, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='portfolio',
            field=models.CharField(choices=[('App', 'App'), ('Card', 'Card'), ('Web', 'Web')], default=1, max_length=256, verbose_name='Our Portfolio'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(default='', upload_to='media/image', verbose_name='Image'),
        ),
    ]