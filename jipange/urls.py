from django.conf.urls import patterns, include, url
from django.conf import settings
from clinics.models import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jipange.views.home', name='home'),
    # url(r'^jipange/', include('jipange.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT
    }),

    url(r'^sms/$', 'jipange.views.reply_to_sms'),


    # Survey tools
    #url(r'^survey/', include('survey.urls')),
    #url(r'^survey/', include('crowdsourcing.urls')),

    url(r'^clinics', include('clinics.urls')),

    # Django CMS
    url(r'^', include('cms.urls')),
)
