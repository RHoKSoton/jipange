from django.conf.urls.defaults import patterns, url
from django.views.generic import DetailView, ListView, TemplateView
from clinics.models import Clinic
import views

urlpatterns = patterns('',

    # Feedback form for anonymous results
    #url('^feedback/?$', TemplateView.as_view(template_name='feedback_form.html')),

    # Find nearest clinic, search for clinics
    #url('^locate/?$', DetailView.as_view(model=Clinic)),

    # List all clinics
    url('^list/?$', ListView.as_view(model=Clinic)),

    # Show clinic details
    url('^detail/(?P<pk>\d+)/?$', DetailView.as_view(model=Clinic)),
    url('^detail/(?P<slug>\d+)/?$', DetailView.as_view(model=Clinic, slug_field='name')),

)
