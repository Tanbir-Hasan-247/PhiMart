from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager

# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email