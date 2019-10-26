from django.db import models
from datetime import datetime

class Post(models.Model):
    
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=2000)
    pic= models.ImageField(upload_to='post_image', blank=True)
    tdate = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

class Contact(models.Model):
    user_name = models.CharField(max_length=50, primary_key=True)
    user_email = models.EmailField(max_length=50)
    user_phone = models.CharField(max_length=50)
    user_desc = models.CharField(max_length=50)    
    def __str__(self):
        return self.user_name
    