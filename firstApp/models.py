from django.db import models

# Create your models here.
# class Portfolio(models.Model):
#     description = models.CharField(max_length=255, blank=True)
#     document = models.FileField(upload_to='documents/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return self.description


class Portfolio(models.Model):
    image = models.ImageField(upload_to='media/image',default='')
    text_field = models.CharField(max_length=200,default='')
    date_added = models.DateTimeField(auto_now_add=False,auto_now=True)
    file_type = models.CharField(max_length=256, choices=[('image', 'image'), ('video', 'video'), ('other', 'other')])
    class Meta:
        verbose_name_plural = "Our Portfolio"
    def __str__(self):
        return self.file_type
