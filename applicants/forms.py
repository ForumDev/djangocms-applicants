from django import forms

from multiupload.fields import MultiFileField

from .models import Applicant, Attachment, Reference


class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['firstname', 'lastname', 'email', 'text']  # not attachments!

    files = MultiFileField(min_num=1, max_num=10, max_file_size=1024*1024*10)

    def save(self, commit=True):
        instance = super(ApplicantForm, self).save(commit)
        for each in self.cleaned_data['files']:
            Attachment.objects.create(file=each, applicant=instance)

        return instance