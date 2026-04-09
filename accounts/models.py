from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin' ,'Admin'),
        ('owner' ,'Owner'),
        ('user'  ,'User'),
    )

    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default='user' )