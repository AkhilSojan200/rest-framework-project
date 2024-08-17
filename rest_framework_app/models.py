from django.db import models

# Create your models here.

class Student(models.Model):

    name = models.CharField(max_length=250)
    address = models.TextField(max_length=250)
    email = models.CharField(max_length=50)