from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    first_name = models.CharField(null=True, blank=True, verbose_name='First name', max_length=100, unique=True)
    last_name = models.CharField(null=True, blank=True, verbose_name='Last name', max_length=100, unique=True)
    username = models.CharField(null=True, blank=True, max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone_number1 = models.CharField(max_length=20, null=False, blank=False, unique=True, verbose_name='Phone Number')
    phone_number2 = models.CharField(max_length=20, null=True, blank=True, unique=True, verbose_name='Phone Number 2')
    side = models.CharField(max_length=100, verbose_name='Side',  blank=True)
    office = models.CharField(max_length=100, verbose_name='Office', blank=True)

    USERNAME_FIELD = 'phone_number1'
    REQUIRED_FIELDS = ['email', 'username']
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.phone_number1
