from django.db import models
from django_twilio.models import Caller


class Message(models.Model):
    received = models.DateTimeField()
    content = models.TextField()
    sender = models.ForeignKey(Caller)
