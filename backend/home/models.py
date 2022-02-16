from django.conf import settings
from django.db import models


class Email(models.Model):
    "Generated Model"
    contact = models.TextField()


class Home1(models.Model):
    "Generated Model"
    email = models.BigIntegerField()
