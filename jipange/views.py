from django.shortcuts import render_to_response
from django.conf import settings


def root(request):
    context = {
        'inbound_number': settings.TWILIO_INBOUND_NUMBER
    }

    if settings.TWILIO_INBOUND_PIN:
        context.update({'inbound_pin': settings.TWILIO_INBOUND_PIN})

    return render_to_response('index.html', context)
