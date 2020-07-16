from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms
from django.views import generic
from django.http import HttpResponse
# Create your views here.


class SignUp(CreateView):
    print("accounts views")
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class Contact(generic.TemplateView):
    template_name = 'accounts/contact.html'
