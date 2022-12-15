from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    is_invalid = models.BooleanField(default=False)
    is_volunteer = models.BooleanField(default=False)


class Invalid(models.Model):
    invalid = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    category_inv = models.CharField(max_length=50)
    limit_inv = models.CharField(max_length=50)
    fio = models.CharField(max_length=50)

    def __str__(self):
        return self.invalid.username


class Volunteer(models.Model):
    volunteer = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    organization_ident = models.CharField(max_length=20, unique=True)
    #is_helping = models.BooleanField(default=False)
    fio = models.CharField(max_length=50)

    def __str__(self):
        return self.volunteer.username


class HelpRequest(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.CharField(max_length=50)
    helper = models.CharField(max_length=50, blank=True)
    owner_accept = models.BooleanField(default=False)
    helper_accept = models.BooleanField(default=False)
    # owner = models.OneToOneField('Invalid', related_name='helprequest', on_delete=models.CASCADE)
    # helper = models.OneToOneField('Volunteer', related_name='helprequest', on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title
