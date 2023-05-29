from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.email

class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    cover_image = models.ImageField(upload_to='/Users/yassinebaazi/Downloads/library-management/media')
    def __str__(self):
        return self.title
