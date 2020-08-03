from django.shortcuts import render
from django.views import generic


class AllBooks(generic.TemplateView):
    template_name = "books/books_all.html"


# Create your views here.
