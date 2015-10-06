from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
import uuid
import os

# from django.utils.http import int_to_base36
# Create your models here.

class Applicant(models.Model):
    firstname = models.CharField(_('First name'), max_length=25,default='')
    lastname = models.CharField(_('Last name'), max_length=25,default='')
    email = models.EmailField(_('Email address'), max_length=255, unique=True,default='')
    text = models.TextField(default='')
    edit_key = models.CharField(max_length=100, unique=True,default=uuid.uuid1)
    
    REQUIRED_FIELDS = ['firstname','lastname','email']
    def __str__(self):              # __unicode__ on Python 2
        return '%s, %s' % (self.lastname, self.firstname)
    def __unicode__(self):
        return '%s, %s' % (self.lastname, self.firstname)
    def get_absolute_url(self):
        return reverse('applicant-view', kwargs={'edit_key': self.edit_key})
#     def __init__(self, *args, **kwargs):
#         super(Applicant, self).__init__()
#         self.edit_key = str(uuid.uuid4())
    
class Reference(models.Model):
    applicant = models.ForeignKey(Applicant, verbose_name=_('Applicant'))
    name = models.CharField(_('Name'), max_length=25)
    email = models.EmailField(_('Email address'), max_length=255, unique=True,default='')
    text = models.TextField(default='')
    edit_key = models.CharField(max_length=100, unique=True,default=uuid.uuid1)
    def __unicode__(self):
        return self.name
    def __str__(self):              # __unicode__ on Python 2
        return self.name
#     def __init__(self, *args, **kwargs):
#         super(Reference, self).__init__()
#         self.edit_key = str(uuid.uuid4())
        
class Attachment(models.Model):
    applicant = models.ForeignKey(Applicant, verbose_name=_('Applicant'))
    file = models.FileField(_('Attachment'), upload_to='media/applicants')
    edit_key = models.CharField(max_length=100, unique=True,default=uuid.uuid1)
    
    def filename(self):
        return os.path.basename(self.file.name)
    
    
    
    
    