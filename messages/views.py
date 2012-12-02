from twilio.twiml import Response
from django_twilio.decorators import twilio_view
from models import *


@twilio_view
def reply_to_sms(request):
    response = Response()

    user, created = PhoneUser.objects.get_or_create(number=request.POST['From'])
    print(user)
    message = IncomingMessage()
    message.content = request.POST['Body']
    message.sender = user
    message.save()

    response.sms('Thank you for your feedback!')
    return response
