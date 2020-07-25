from django.db import models 
from django.contrib.auth.models import User
from django import forms
from datetime import date


class BlogDetails(models.Model):
    author_username = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    blog = models.TextField()
    posted_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
      return self.title



class UserInfo(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  date_of_birth = models.DateField()
  bio = models.CharField(max_length=150,default="No Bio")
  profile_picture = models.ImageField(default='null-user-image.jpg')
  
  def __str__(self):
    return self.user.email
