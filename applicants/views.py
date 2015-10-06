from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import FormView, CreateView
from django.views.generic import DetailView, UpdateView, DeleteView

from .forms import ApplicantCreateForm, ApplicantUpdateForm, AttachmentUpdateForm, AttachmentCreateForm
from .models import Applicant, Attachment
from django.core.urlresolvers import reverse


class ApplicantCreateView(CreateView):
    model = Applicant
    form_class = ApplicantCreateForm
    template_name = 'applicant/form.html'
#     success_url = get_success_url(self)
    def get_success_url(self): 
        return reverse('applicant-view', kwargs={'edit_key': self.object.edit_key})
    
class ApplicantDetailView(DetailView):
    model = Applicant
    template_name = 'applicant/view.html'
    
    def get_object(self):
        return Applicant.objects.get(edit_key=self.kwargs['edit_key'])
    
    def get_context_data(self, **kwargs):
        context = super(ApplicantDetailView, self).get_context_data(**kwargs)
        context['attachments'] = Attachment.objects.filter(applicant=self.get_object().id)
#         context['action'] = reverse('applicant-edit',
#                                     kwargs={'edit_key': self.get_object().edit_key})
        return context
    
class ApplicantUpdateView(UpdateView):

    model = Applicant
    template_name = 'applicant/form.html'
    form_class = ApplicantUpdateForm
    def get_success_url(self):
        return reverse('applicant-view', kwargs={'edit_key': self.get_object().edit_key})
    
    def get_object(self):
        return Applicant.objects.get(edit_key=self.kwargs['edit_key'])

    def get_context_data(self, **kwargs):
        context = super(ApplicantUpdateView, self).get_context_data(**kwargs)
#         context.update({'instance': instance
#             , 'attachments': models.Attachment.objects.get(applicant=self.get_object().id)})
        context['action'] = reverse('applicant-edit',
                                    kwargs={'edit_key': self.get_object().edit_key})
        return context
    
# class ApplicantDeleteView(DeleteView):
# 
#     model = Applicant
#     template_name = 'applicant/delete.html'
# 
#     def get_success_url(self):
#         return '/'
#     
#     def get_object(self):
#         return Applicant.objects.get(edit_key=self.kwargs['edit_key'])
    
    
    
class AttachmentCreateView(CreateView):
    model = Applicant
    form_class = AttachmentCreateForm
    template_name = 'applicant/form.html'
#     success_url = get_success_url(self)
    def get_success_url(self): 
        return reverse('applicant-view', kwargs={'edit_key': self.kwargs['edit_key']})
    def form_valid(self, form):
        attachment = form.save(commit=False)
        attachment.applicant = Applicant.objects.get(edit_key=self.kwargs['edit_key'])
        return super(AttachmentCreateView, self).form_valid(form)
    
class AttachmentUpdateView(UpdateView):

    model = Attachment
    template_name = 'applicant/form.html'
    form_class = AttachmentUpdateForm
    def get_success_url(self):
        return reverse('applicant-view', kwargs={'edit_key': self.get_object().applicant.edit_key})
    
    def get_object(self):
        return Attachment.objects.get(edit_key=self.kwargs['edit_key'])

class AttachmentDeleteView(DeleteView):

    model = Attachment
    template_name = 'attachment/delete.html'

    def get_success_url(self):
        return reverse('applicant-view', kwargs={'edit_key': self.get_object().applicant.edit_key})
    
    def get_object(self):
        return Attachment.objects.get(edit_key=self.kwargs['edit_key'])
    
    
    