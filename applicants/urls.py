from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^apply', views.ApplicantCreateView.as_view(), name='applicant-apply'),
    url(r'^view/(?P<edit_key>[\w\d-]+)', views.ApplicantDetailView.as_view(), name='applicant-view'),
    url(r'^edit/(?P<edit_key>[\w\d-]+)', views.ApplicantUpdateView.as_view(), name='applicant-edit',),
    url(r'^attachment/edit/(?P<edit_key>[\w\d-]+)', views.AttachmentUpdateView.as_view(), name='attachment-edit',),
    url(r'^attachment/add/(?P<edit_key>[\w\d-]+)', views.AttachmentCreateView.as_view(), name='attachment-add',),
    url(r'^attachment/delete/(?P<edit_key>[\w\d-]+)', views.AttachmentDeleteView.as_view(), name='attachment-delete',),
#     url(r'^apply\.html/save_applicant$', views.ApplicantView.as_view(), name='apply'),
]