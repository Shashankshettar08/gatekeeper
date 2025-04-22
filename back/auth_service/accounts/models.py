from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    usn = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)