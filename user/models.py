from django.db import models
from django.forms import EmailField
from helpers.models import TrackingModel
from django.contrib.auth.models import PermissionsMixin,BaseUserManager,AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
# Create your models here.



class User(AbstractBaseUser,PermissionsMixin,TrackingModel):
    
    username_validator=UnicodeUsernameValidator()
    username =models.CharField(
        ('username'),
        max_length=150,
        unique=True,
        help_text=('Required.150 characters or fewer'),
        validators=[username_validator],
        error_messages={
            'unique':("A user with that username already exist"),
        },
    )

    email = models.EmailField(('email adress'), blank=True, unique=True)
     
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    date_joined=models.DateTimeField(('date joined'), default=True)
    
    objects =UserManager()

    EmailField = 'email'
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS =['username']