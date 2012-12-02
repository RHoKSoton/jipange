from django.contrib import admin
import models


admin.site.register(models.IncomingMessage)
admin.site.register(models.PhoneUser)
admin.site.register(models.OutgoingMessage)
admin.site.register(models.MessagingList)
