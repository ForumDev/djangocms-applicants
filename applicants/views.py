from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import FormView, CreateView
from django.views.generic import DetailView, UpdateView, DeleteView

from .forms import ApplicantCreateForm, ApplicantUpdateForm
from .forms import AttachmentUpdateForm, AttachmentCreateForm
from .forms import ReferencePrivateUpdateForm, ReferenceUpdateForm, ReferenceCreateForm
from .forms import ScoreCreateForm, ScoreUpdateForm
from .forms import NoteCreateForm

from .models import Applicant, Attachment, Reference, Event, Score, Note
from myauth.models import User
from django.core.urlresolvers import reverse


class ApplicantCreateView(CreateView):
    model = Applicant
    form_class = ApplicantCreateForm
    template_name = 'applicant/form.html'
    def get_success_url(self): 
        return reverse('applicant-view', kwargs={'edit_key': self.object.edit_key})
#     def get_initial(self):
#         return {"event": Event.objects.get(abbr=self.kwargs['event_abbr']).id}
    def form_valid(self, form):
        applicant = form.save(commit=False)
        applicant.event = Event.objects.get(abbr=self.kwargs['event_abbr'])
        return super(ApplicantCreateView, self).form_valid(form)
    
class ApplicantDetailView(DetailView):
    model = Applicant
    template_name = 'applicant/view.html'
    
    def get_object(self):
        return Applicant.objects.get(edit_key=self.kwargs['edit_key'])
    
    def get_context_data(self, **kwargs):
        context = super(ApplicantDetailView, self).get_context_data(**kwargs)
        context['attachments'] = Attachment.objects.filter(applicant=self.get_object().id)
        context['references'] = Reference.objects.filter(applicant=self.get_object().id)
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





class ReferenceCreateView(CreateView):
    model = Reference
    form_class = ReferenceCreateForm
    template_name = 'reference/create.html'
#     success_url = get_success_url(self)
    def get_success_url(self): 
        return reverse('applicant-view', kwargs={'edit_key': self.kwargs['edit_key']})
    def form_valid(self, form):
        reference = form.save(commit=False)
        reference.applicant = Applicant.objects.get(edit_key=self.kwargs['edit_key'])
        return super(ReferenceCreateView, self).form_valid(form)
    
class ReferenceUpdateView(UpdateView):
    model = Reference
    template_name = 'reference/edit.html'
    form_class = ReferenceUpdateForm
    def get_success_url(self):
        return reverse('applicant-view', kwargs={'edit_key': self.get_object().applicant.edit_key})
    
    def get_object(self):
        return Reference.objects.get(edit_key=self.kwargs['edit_key'])
    
class ReferencePrivateUpdateView(UpdateView):
    model = Reference
    template_name = 'applicant/form.html'
    form_class = ReferencePrivateUpdateForm
    def get_success_url(self):
        return reverse('applicant-view', kwargs={'edit_key': self.get_object().applicant.edit_key})
    
    def get_object(self):
        return Reference.objects.get(pedit_key=self.kwargs['pedit_key'])

class ReferenceDeleteView(DeleteView):
    model = Reference
    template_name = 'reference/delete.html'

    def get_success_url(self):
        return reverse('applicant-view', kwargs={'edit_key': self.get_object().applicant.edit_key})
    
    def get_object(self):
        return Reference.objects.get(edit_key=self.kwargs['edit_key'])
    
    
class EventDetailView(DetailView):
    model = Event
    template_name = 'voting/event.html'
    
    def get_object(self):
        return Event.objects.get(abbr=self.kwargs['abbr'])
    
    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['applicants'] = Applicant.objects.filter(event=self.get_object().id)
        context['references'] = Reference.objects.all
        context['attachments'] = Attachment.objects.all
        context['users'] = User.objects.all ## add filter is_voter
        context['scores'] = Score.objects.all
        context['notes'] = Note.objects.all
#         if request.user.is_authenticated():
            
        return context
    
    
class ScoreCreateView(CreateView):
    model = Score
    form_class = ScoreCreateForm
    template_name = 'applicant/form.html'
#     success_url = get_success_url(self)
    def get_success_url(self): 
        return reverse('voting-event', kwargs={'abbr': self.kwargs['abbr']})
    def form_valid(self, form):
        score = form.save(commit=False)
        score.user = self.request.user
        score.applicant = Applicant.objects.get(pk=self.kwargs['appid'])
        return super(ScoreCreateView, self).form_valid(form)
    
class ScoreUpdateView(UpdateView):
    model = Score
    template_name = 'applicant/form.html'
    form_class = ScoreUpdateForm
    def get_success_url(self):
        return reverse('voting-event', kwargs={'abbr': self.kwargs['abbr']})
    def get_object(self):
        return Score.objects.get(pk=self.kwargs['scoreid'])
    
    
class NoteCreateView(CreateView):
    model = Note
    form_class = NoteCreateForm
    template_name = 'applicant/form.html'
#     success_url = get_success_url(self)
    def get_success_url(self): 
        return reverse('voting-event', kwargs={'abbr': self.kwargs['abbr']})
    def form_valid(self, form):
        note= form.save(commit=False)
        note.user = self.request.user
        note.applicant = Applicant.objects.get(pk=self.kwargs['appid'])
        return super(NoteCreateView, self).form_valid(form)
    
    