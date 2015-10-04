from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^apply\.html', views.ApplicantView.as_view()),
]