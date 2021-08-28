from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from .forms import PDEUCreationForm


class SignUp(generic.CreateView):
    form_class = PDEUCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'



