from django.db import models
from helpers.models import TrackingModel
from django.contrib.auth.models import PermissionsMixin,BaseUserManager,AbstractBaseUser

# Create your models here.

class User(AbstractBaseUser,PermissionsMixin,TrackingModel):
    pass