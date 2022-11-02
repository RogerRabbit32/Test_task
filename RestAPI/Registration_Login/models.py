from django.db import models


class User(models.Model):
    phone = models.CharField(max_length=20, blank=False, unique=True)
    login = models.CharField(max_length=20, blank=False, unique=True)
    password = models.CharField(max_length=20, blank=False)
    name = models.CharField(max_length=20, blank=False)
    birth = models.DateField(blank=False)
    tg = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True, null=True)

