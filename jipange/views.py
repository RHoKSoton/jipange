from twilio.twiml import Response
from django_twilio.decorators import twilio_view


@twilio_view
def reply_to_sms(request):
    r = Response()
    r.sms('Thanks for the message!')
    return r
