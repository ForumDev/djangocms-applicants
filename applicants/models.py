from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
import uuid

# from django.utils.http import int_to_base36
# Create your models here.

class Applicant(models.Model):
    firstname = models.CharField(_('First name'), max_length=25)
    lastname = models.CharField(_('Last name'), max_length=25)
    email = models.EmailField(_('Email address'), max_length=255, unique=True,default='')
    text = models.TextField(default='')
    edit_key = models.CharField(max_length=100, null=True, blank=True, unique=True)
    def __init__(self):
        super(Applicant, self).__init__()
        self.edit_key = str(uuid.uuid4())
    def __str__(self):              # __unicode__ on Python 2
        return self.lastname+ ', ' + self.firstname
    def __unicode__(self):
        return self.lastname+ ', ' + self.firstname
    
class Reference(models.Model):
    applicant = models.ForeignKey(Applicant, verbose_name=_('Applicant'))
    name = models.CharField(_('Name'), max_length=25)
    email = models.EmailField(_('Email address'), max_length=255, unique=True,default='')
    text = models.TextField(default='')
    edit_key = models.CharField(max_length=100, null=True, blank=True, unique=True)
    def __str__(self):              # __unicode__ on Python 2
        return self.name
    def __init__(self):
        super(Reference, self).__init__()
        self.edit_key = str(uuid.uuid4())
    def __unicode__(self):
        return self.name
    
class Attachment(models.Model):
    applicant = models.ForeignKey(Applicant, verbose_name=_('Applicant'))
    file = models.FileField(_('Attachment'), upload_to='media/applicants')
    
    
    
    
    