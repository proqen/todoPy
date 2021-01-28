from django.db import models

# Create your models here.

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class Book(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year = models.DateField(auto_now_add=False)
    date = models.DateField(auto_now_add=True)
    is_favorite = models.BooleanField(default=False)
