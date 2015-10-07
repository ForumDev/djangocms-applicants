from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from datetime import datetime
from myauth.models import User
import uuid
import os

# from django.utils.http import int_to_base36
# Create your models here.

class Event(models.Model):
    title = models.CharField(_('Event title'), max_length=255,default='')
    abbr = models.CharField(_('Short acronym (max 20 characters)'), max_length=20, unique=True)
    begin_date = models.DateField(_('Event begin date'), blank=True, null=True)
    end_date = models.DateField(_('Event end date'), blank=True, null=True)
    app_begin_date = models.DateField(_('Application begin date'), blank=True, null=True)
    app_end_date = models.DateField(_('Application end date'), blank=True, null=True)
    def __unicode__(self):
        if not self.abbr:
            return self.title
        else: 
            return self.abbr
    def __str__(self):              
        if not self.abbr:
            return self.title
        else: 
            return self.abbr

class Applicant(models.Model):
    firstname = models.CharField(_('First name'), max_length=25,default='')
    lastname = models.CharField(_('Last name'), max_length=25,default='')
    email = models.EmailField(_('Email address'), max_length=255, unique=True,default='')
    text = models.TextField(default='')
    edit_key = models.CharField(max_length=100, unique=True,default=uuid.uuid1)
    #probably should remove the blank from foreign key
    event = models.ForeignKey(Event, verbose_name=_('Event'), blank=True, null=True)
    
    REQUIRED_FIELDS = ['firstname','lastname','email']
    def __str__(self):              
        return '%s, %s' % (self.lastname, self.firstname)
    def __unicode__(self):
        return '%s, %s' % (self.lastname, self.firstname)
    def get_absolute_url(self):
        return reverse('applicant-view', kwargs={'edit_key': self.edit_key})
#     def __init__(self, *args, **kwargs):
#         super(Applicant, self).__init__()
#         self.edit_key = str(''())
    
class Reference(models.Model):
    #probably should remove the blank from foreign key
    applicant = models.ForeignKey(Applicant, verbose_name=_('Applicant'), blank=True)
    name = models.CharField(_('Name'), max_length=25)
    email = models.EmailField(_('Email address'), max_length=255, unique=True,default='')
    text = models.TextField(_('Reference letter'), default='')
    edit_key = models.CharField(max_length=100, unique=True,default=uuid.uuid1)
    pedit_key = models.CharField(max_length=100, unique=True,default=uuid.uuid4)
    def __unicode__(self):
        return self.name
    def __str__(self):              
        return self.name
#     def __init__(self, *args, **kwargs):
#         super(Reference, self).__init__()
#         self.edit_key = str(''())
        
class Attachment(models.Model):
    applicant = models.ForeignKey(Applicant, verbose_name=_('Applicant'), blank=True)
    file = models.FileField(_('Attachment'), upload_to='media/applicants')
    edit_key = models.CharField(max_length=100, unique=True,default=uuid.uuid1)
    
    def filename(self):
        return os.path.basename(self.file.name)
    
    
class Score(models.Model):
    SCORE_CHOICES = (
      (1, '1 (best)'),
      (2, '2'),
      (3, '3'),
      (4, '4'),
      (5, '5'),
      (6, '6'),
      (7, '7'),
      (8, '8'),
      (9, '9'),
      (10, '10 (worst)'),
    )
    score = models.IntegerField(_('Score'), choices=SCORE_CHOICES)
    user = models.ForeignKey(User, verbose_name=_('Voter'), blank=True)
    applicant = models.ForeignKey(Applicant, verbose_name=_('Applicant'), blank=True)
    def __unicode__(self):
        return self.user.last_name+': '+str(self.score)+' ('+self.applicant.lastname+', '+self.applicant.firstname+')'
    def __str__(self):              
        return self.user.last_name+': '+str(self.score)+' ('+self.applicant.lastname+', '+self.applicant.firstname+')'
    
class Note(models.Model):
    note = models.TextField(_('Note'), default='')
    user = models.ForeignKey(User, verbose_name=_('Voter'), blank=True)
    applicant = models.ForeignKey(Applicant, verbose_name=_('Applicant'), blank=True)
    created = models.DateTimeField(_("Date time"), default=datetime.now())
    def __unicode__(self):
        return self.user.last_name+': '+str(self.id)+' ('+self.applicant.lastname+', '+self.applicant.firstname+')'
    def __str__(self):              
        return self.user.last_name+': '+str(self.id)+' ('+self.applicant.lastname+', '+self.applicant.firstname+')'
    
    
    