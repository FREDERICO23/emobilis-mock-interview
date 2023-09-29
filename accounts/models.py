from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userprofile")
    avatar = models.FileField(upload_to="avatars/", null=True)
    name =  models.CharField(max_length=50, null=True)
    bio = models.CharField(max_length=500, null=True)

class Post(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True) 
   
    def __str__(self):
        return self.name