from django.urls import path

from . import views

app_name = 'books'


urlpatterns = [path("books_all", views.AllBooks.as_view(), name="books_all"), ]
