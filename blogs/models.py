from django.db import models

# Create your models here.
class Blogs(models.Model):
    title = models.TextField()
    author = models.TextField()
    content = models.TextField()