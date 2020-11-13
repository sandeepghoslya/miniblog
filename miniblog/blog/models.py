from django.db import models


# Create your models here.
class Post(models.Model):
    objects = None
    title = models.CharField(max_length=150)
    desc = models.TextField()