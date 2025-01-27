from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE,verbose_name='用户')
    email = models.EmailField(max_length=254,unique=True)
    nike_name = models.CharField(max_length=20)

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