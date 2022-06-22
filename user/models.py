from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.

class User(AbstractUser):
    '''Define user authorisation and permission rules'''
    is_client = models.BooleanField(default=False)
    is_counsellor = models.BooleanField(default=False)

# Client profile
class ClientProfile(models.Model):
    '''
    Client profile has a relationship with the Django User model from auth.
    From the User model we get a username, email and password.
    Client profile will collect more informations about the person seeking counselling.
    '''
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    prof_pic = models.ImageField(blank=True, upload_to='media')
    about_me = models.TextField(blank=True, max_length=255)
    full_name = models.CharField(blank=True,max_length=50)

    def __str__(self):
        '''Display full_name field on the database ORM'''
        return self.full_name

    def save_client_profile(self):
        '''Add Profile to database'''
        self.save()
