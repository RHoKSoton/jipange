from django.db import models


class PhoneUser(models.Model):
    number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=30)


class Message(models.Model):
    received = models.DateTimeField()
    content = models.TextField()
    sender = models.ForeignKey(PhoneUser)
