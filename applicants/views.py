from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import FormView, CreateView

from .forms import ApplicantForm
from .models import Applicant


class ApplicantView(CreateView):
    model = Applicant
    form_class = ApplicantForm
    template_name = 'applicant_form/form.html'
    success_url = '?success'