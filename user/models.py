from django.db import models
from django.forms import EmailField
from helpers.models import TrackingModel
from django.contrib.auth.models import PermissionsMixin,BaseUserManager,AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        
        if not username:
            raise TypeError('The given username must be set')

        if not email:
            raise ValueError(('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email,)
        user.set_password(password)
        user.save()
        return user
       

    def create_superuser(self, username, email, password):
     
      if password is None:
          raise TypeError('Superusers must have a password.')

      user = self.create_user(username, email, password)
      user.is_superuser = True
      user.is_staff = True
      user.save()

      return user


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
    email_verified=models.BooleanField(
        ('email_verified'),
        default=False,
        help_text=('Confirm whether this users email is verified')
    )
    objects =UserManager()

    EmailField = 'email'
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS =['username']