from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    short_text  =models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    author = models.IntegerField(default=1)
