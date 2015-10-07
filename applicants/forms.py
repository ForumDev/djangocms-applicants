from django import forms

from multiupload.fields import MultiFileField
from crispy_forms.helper import FormHelper                                                
from crispy_forms.layout import Layout, HTML, Submit, Fieldset

from .models import Applicant, Attachment, Reference, Score, Note


class ReferenceUpdateForm(forms.ModelForm):
    class Meta:
        model = Reference
        exclude = ['applicant','edit_key', 'pedit_key', 'text']
        
class ReferencePrivateUpdateForm(forms.ModelForm):
    class Meta:
        model = Reference
        exclude = ['applicant','edit_key', 'pedit_key']

class ReferenceCreateForm(forms.ModelForm):
    class Meta:
        model = Reference
        exclude = ['applicant','edit_key', 'pedit_key','text']
        
           
class AttachmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Attachment
        exclude = ['applicant','edit_key']

class AttachmentCreateForm(forms.ModelForm):
    class Meta:
        model = Attachment
        exclude = ['applicant','edit_key']
        

class ApplicantUpdateForm(forms.ModelForm):
    class Meta:
        model = Applicant
        exclude = ['event', 'edit_key']
        
class ApplicantCreateForm(forms.ModelForm):
    class Meta:
        model = Applicant
        exclude = ['event', 'edit_key']  # not attachments!

#     files = MultiFileField(min_num=1, max_num=10, max_file_size=1024*1024*10)
#     
#     def save(self, commit=True):
#         instance = super(ApplicantCreateForm, self).save(commit)
#         for each in self.cleaned_data['files']:
#             Attachment.objects.create(file=each, applicant=instance)
#   
#         return instance

class ScoreCreateForm(forms.ModelForm):
    class Meta:
        model = Score
        exclude = ['user','applicant']
        

class ScoreUpdateForm(forms.ModelForm):
    class Meta:
        model = Score
        exclude = ['user','applicant']
        
class NoteCreateForm(forms.ModelForm):
    class Meta:
        model = Note
        exclude = ['user','applicant','created']