from django.views import generic
# from .photodictionary import photosetup
# from . import photodictionary

from django.shortcuts import render
# Create your views here.

# class FashionPhotos(generic.TemplateView):
#     template_name = "photography/fashion_photos.html"

# class FashionPhotos(generic.TemplateView):
#     template_name = "photography/fashion_photos.html"


class AllPhotos(generic.TemplateView):
    template_name = "photography/photos_all.html"


class KidsPhotos(generic.TemplateView):
    template_name = "photography/kids_photos.html"


class BeautyPhotos(generic.TemplateView):
    template_name = "photography/beauty_photos.html"


class PortraitPhotos(generic.TemplateView):
    template_name = "photography/portrait_photos.html"


class TheaterPhotos(generic.TemplateView):
    template_name = "photography/theater_photos.html"


class FoodPhotos(generic.TemplateView):
    template_name = "photography/food_photos.html"
