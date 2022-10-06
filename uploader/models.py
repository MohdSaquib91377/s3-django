from distutils.command.upload import upload
from django.db import models
# Create your models here.
class DropBoxer(models.Model):
    title = models.CharField(max_length = 64)
    document = models.FileField(max_length = 500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Drop Boxes'