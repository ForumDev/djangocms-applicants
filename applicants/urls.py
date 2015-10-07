from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views


urlpatterns = [
    url(r'^apply/(?P<event_abbr>[\w\d-]+)', views.ApplicantCreateView.as_view(), name='applicant-apply'),
    url(r'^view/(?P<edit_key>[\w\d-]+)', views.ApplicantDetailView.as_view(), name='applicant-view'),
    url(r'^edit/(?P<edit_key>[\w\d-]+)', views.ApplicantUpdateView.as_view(), name='applicant-edit',),
    
    url(r'^attachment/edit/(?P<edit_key>[\w\d-]+)', views.AttachmentUpdateView.as_view(), name='attachment-edit',),
    url(r'^attachment/add/(?P<edit_key>[\w\d-]+)', views.AttachmentCreateView.as_view(), name='attachment-add',),
    url(r'^attachment/delete/(?P<edit_key>[\w\d-]+)', views.AttachmentDeleteView.as_view(), name='attachment-delete',),

    url(r'^reference/edit/(?P<edit_key>[\w\d-]+)', views.ReferenceUpdateView.as_view(), name='reference-edit',),
    url(r'^reference/pedit/(?P<pedit_key>[\w\d-]+)', views.ReferencePrivateUpdateView.as_view(), name='reference-pedit',),
    url(r'^reference/add/(?P<edit_key>[\w\d-]+)', views.ReferenceCreateView.as_view(), name='reference-add',),
    url(r'^reference/delete/(?P<edit_key>[\w\d-]+)', views.ReferenceDeleteView.as_view(), name='reference-delete',),
    
    url(r'^voting/event/(?P<abbr>[\w\d-]+)', login_required(views.EventDetailView.as_view()), name='voting-event',),
    
    url(r'^voting/score/add/(?P<abbr>[\w\d-]+)/(?P<appid>[\w\d-]+)', login_required(views.ScoreCreateView.as_view()), name='voting-add-score',),
    url(r'^voting/score/update/(?P<abbr>[\w\d-]+)/(?P<scoreid>[\w\d-]+)', login_required(views.ScoreUpdateView.as_view()), name='voting-edit-score',),

    url(r'^voting/note/add/(?P<abbr>[\w\d-]+)/(?P<appid>[\w\d-]+)', login_required(views.NoteCreateView.as_view()), name='voting-add-note',),
]