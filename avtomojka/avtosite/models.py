from django.contrib import auth
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Service(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    price = models.FloatField()

    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'


class Applications(models.Model):
    service = models.ForeignKey('Service', on_delete=models.PROTECT)
    client = models.ForeignKey(User, blank=True, on_delete=models.PROTECT)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Заявки'
        verbose_name_plural = 'Заявки'
        ordering = ['-time_create']


