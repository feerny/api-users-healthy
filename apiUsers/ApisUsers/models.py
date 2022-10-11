from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=70,unique=True, blank=False, default='')
    email = models.CharField(max_length=70, unique=True, blank=False, default='')
    password = models.CharField(max_length=70, blank=False, default='')
    def __str__(self):
          
        return self.name