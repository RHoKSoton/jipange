from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from twilio.rest import TwilioRestClient


class PhoneUser(models.Model):
    number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=30, blank=True, null=True)

    def __unicode__(self):
        return self.name if self.name else self.number


class IncomingMessage(models.Model):
    received = models.DateTimeField(auto_now=True)
    content = models.TextField()
    sender = models.ForeignKey(PhoneUser)

    def __unicode__(self):
        return u'%s - %s' % (self.sender, self.content)


class MessagingList(models.Model):
    name = models.CharField(max_length=30)
    users = models.ManyToManyField(PhoneUser)

    def __unicode__(self):
        return self.name


class OutgoingMessage(models.Model):
    sent = models.DateTimeField(auto_now=True)
    messaged_list = models.ForeignKey(MessagingList)
    content = models.CharField(max_length=160)

    def __unicode__(self):
        return u'%s - %s' % (self.messaged_list, self.content)


def send_message(sender, instance, **kwargs):
    if not kwargs.get('created'):
        return False

    client = TwilioRestClient(
        settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    phones = instance.messaged_list.users.all()
    for phone in phones:
        client.sms.messages.create(
            to=phone.number,
            body=instance.content,
            from_=settings.TWILIO_NUMBER)

post_save.connect(send_message, sender=OutgoingMessage)
