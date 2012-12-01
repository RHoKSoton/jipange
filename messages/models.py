from django.db import models


class PhoneUser(models.Model):
    number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name if self.name else self.number


class Message(models.Model):
    received = models.DateTimeField(auto_now=True)
    content = models.TextField()
    sender = models.ForeignKey(PhoneUser)

    def __unicode__(self):
        return u'%s - %s' % (self.sender, self.content)
