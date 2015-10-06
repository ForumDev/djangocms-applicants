from django import forms

from multiupload.fields import MultiFileField
from crispy_forms.helper import FormHelper                                                
from crispy_forms.layout import Layout, HTML, Submit, Fieldset

from .models import Applicant, Attachment, Reference


class ApplicantUpdateForm(forms.ModelForm):
    class Meta:
        model = Applicant
        exclude = ['edit_key']
        
class AttachmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Attachment
        exclude = ['applicant','edit_key']

class AttachmentCreateForm(forms.ModelForm):
    class Meta:
        model = Attachment
        exclude = ['applicant','edit_key']
        
#     files = MultiFileField(min_num=1, max_num=10, max_file_size=1024*1024*10)
#     
#     def save(self, commit=True):
#         instance = super(ApplicantForm, self).save(commit)
#         for each in self.cleaned_data['files']:
#             Attachment.objects.create(file=each, applicant=instance)
#   
#         return instance
        
class ApplicantCreateForm(forms.ModelForm):
    class Meta:
        model = Applicant
        exclude = ['edit_key']  # not attachments!

    files = MultiFileField(min_num=1, max_num=10, max_file_size=1024*1024*10)
    
    def save(self, commit=True):
        instance = super(ApplicantCreateForm, self).save(commit)
        for each in self.cleaned_data['files']:
            Attachment.objects.create(file=each, applicant=instance)
  
        return instance