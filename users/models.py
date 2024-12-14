from django.contrib.auth.models import AbstractUser
from django.db import models

from mailings.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    name = models.CharField(max_length=50, verbose_name='имя пользователя', **NULLABLE)
    avatar = models.ImageField(upload_to='users/avatars/%Y-%m-%d/', verbose_name='аватар', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []