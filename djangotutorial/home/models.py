from django.db import models

# Create your models here.
class UserProfile(models.Model):
    nike_name = models.CharField(max_length=20)
    # username = models.CharField(max_length=20)
    # password = models.CharField(max_length=20)

class Comment(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     date = models.DateTimeField(auto_now_add=True)
#     author = models.CharField(max_length=20)
#     comment = models.ManyToManyField(Comment, blank=True)