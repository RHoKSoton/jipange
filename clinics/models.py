from django.db import models
from geoposition.fields import GeopositionField
from django import forms

class Clinic(models.Model):
    """
    A clinic providing health services.
    """

    name = models.CharField(
      'Name of the clinic',
      max_length = 255,
      unique = True,
    )

    location = GeopositionField(
      'Physical location of the clinic'
    )

    opening_times = models.CharField(
      'Clinic opening hours and days',
      max_length = 255
    )

    services_provided = models.ManyToManyField(
      'ClinicService',
    )

    def __unicode__(self):
        return self.name


class ClinicService(models.Model):
    """
    A health service provided by a clinic.
    """

    name = models.CharField(
      'Short name for the service',
      max_length = 50,
      unique = True,
    )

    description = models.CharField(
      'Longer description of the service provided',
      max_length = 255
    )

    def __unicode__(self):
        return self.name


class ClinicFeedback(models.Model):
    """
    A feedback submission for a clinic.
    """

    clinic = models.ForeignKey(Clinic)

    visit_date = models.DateField(
      'Date of visit'
    )

    patient_age = models.IntegerField(
      'Your age (years)',
      blank = True, null = True,
    )

    patient_sex = models.CharField(
      'Your sex (gender)',
      blank = True, null = True,
      max_length = 1,
      choices = (
        ('M', 'Male'),
        ('F', 'Female'),
      )
    )


    services_needed = models.ManyToManyField(
      'ClinicService',
      blank = True, null = True,
    )

    provider_sex = models.CharField(
      'Provider\'s sex (gender)',
      blank = True, null = True,
      max_length = 1,
      choices = (
        ('M', 'Male'),
        ('F', 'Female'),
      ),
      #widget = forms.RadioSelect(),
    )

    free_questions = models.CharField(
      'Were you free to ask any questions you had?',
      max_length = 1,
      choices = (
        ('Y', 'Yes'),
        ('S', 'Somewhat'),
        ('N', 'No'),
      ),
      blank = True, null = True,
    )
    
    got_info = models.CharField(
      'Did you get the information you wanted?',
      max_length = 1,
      choices = (
        ('Y', 'Yes'),
        ('S', 'Somewhat'),
        ('N', 'No'),
      ),
      blank = True, null = True,
    )
    
    got_supplies = models.CharField(
      'Did you get the supplies you wanted?',
      max_length = 1,
      choices = (
        ('Y', 'Yes'),
        ('N', 'No'),
        ('X', 'Didn\'t want any'),
      ),
      blank = True, null = True,
    )

    harsh_provider = models.CharField(
      'Was any provider harsh or made you feel ashamed?',
      max_length = 1,
      choices = (
        ('Y', 'Yes'),
        ('S', 'Somewhat'),
        ('N', 'No'),
      ),
      blank = True, null = True,
    )
    
    enough_privacy = models.CharField(
      'Did you have enough privacy?',
      max_length = 1,
      choices = (
        ('Y', 'Yes'),
        ('S', 'Somewhat'),
        ('N', 'No'),
      ),
      blank = True, null = True,
    )
    
    pal_provided = models.NullBooleanField(
      'Did a PAL provide services to you within the facility?'
    )

    waiting_time = models.IntegerField(
      'About how long did you have to wait? (minutes)',
      blank = True, null = True,
    )

    cost = models.IntegerField(
      'What did you pay for services, if anything?',
      blank = True, null = True,
    )

    recommended = models.CharField(
      'Would you recommend this place to other youths?',
      max_length = 1,
      choices = (
        ('Y', 'Yes'),
        ('M', 'Maybe'),
        ('N', 'No'),
      ),
      blank = True, null = True,
    )

    why_recommend = models.CharField(
      'Why or why not?',
      max_length = 255,
      blank = True, null = True,
    )
