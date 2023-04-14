from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=20)
    last_login = models.DateTimeField(auto_now=True)
    is_superuser = models.BooleanField(default=False)
    
    
class user_followings(models.Model):
    # followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    from_user_id = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')
    to_user_id = models.ManyToManyField(User, related_name='followers')