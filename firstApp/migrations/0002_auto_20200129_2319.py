# Generated by Django 3.0.2 on 2020-01-29 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portfolio',
            options={'verbose_name_plural': 'Files Manager'},
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='description',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='document',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='uploaded_at',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='date_added',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='file_type',
            field=models.CharField(choices=[('image', 'image'), ('video', 'video'), ('other', 'other')], default=1, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(default='', upload_to='media/image'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='text_field',
            field=models.CharField(default='', max_length=200),
        ),
    ]