from django.conf import settings
from django.db import models
from django.utils import timezone

class Notes4(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    tags=models.CharField(max_length=200)
    uploader=models.CharField(max_length=200)
    def publish(self):
        self.save()
    def __str__(self):
        return self.title
# Create your models here.
