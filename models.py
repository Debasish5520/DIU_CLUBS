from django.db import models
from django.contrib.auth.models import AbstractUser

class Club(models.Model):
    club_name = models.CharField(max_length=50,unique=True,blank=False)
    image = models.ImageField(upload_to='club_image', height_field=None, width_field=None, max_length=None)
    about_club = models.CharField(max_length=200,blank=False)
    club_link = models.URLField(max_length=200,unique=True)
    
    
    def __str__(self):
        return self.club_name
    
class Notice(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    
    def __str__(self):
        return self.title
    
    
    