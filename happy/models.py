from django.db import models
from django.contrib .auth.models import User
# Create your models here.
class Contact(models.Model):
    owner = models.ForeignKey(to=User,on_delete=models.CASCADE)
    firstname= models.CharField(max_length=150)
    lastname= models.CharField(max_length=150)
    email= models.CharField(max_length=150)
    phone_number= models.CharField(max_length=150)
    loacation= models.CharField(max_length=150)
