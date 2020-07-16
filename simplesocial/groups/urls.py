from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'groups'
print("APP NAME GROUP")
urlpatterns = [
    url(r"^$", views.ListGroup.as_view(), name="all"),
    url(r"^new/$", views.CreateGroup.as_view(), name="create"),
    url(r"^posts/in/(?P<slug>[-\w]+)/$",views.SingleGroup.as_view(),name="single"),
    url(r"join/(?P<slug>[-\w]+)/$",views.JoinGroup.as_view(),name="join"),
    #path("join/<slug:slug>",views.JoinGroup.as_view(),name="join"),
    url(r"leave/(?P<slug>[-\w]+)/$",views.LeaveGroup.as_view(),name="leave"),
    url(r"delete/(?P<slug>[-\w]+)/$",views.DeleteGroup.as_view(),name="delete"),
]
