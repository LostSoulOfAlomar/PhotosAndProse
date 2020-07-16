from django.conf.urls import url
from django.urls import path

from . import views

app_name='posts'
print("post urls")
urlpatterns = [
    path('', views.PostList.as_view(), name="all"),
    url(r"new/$", views.CreatePost.as_view(), name="create"),
    url(r"by/(?P<username>[-\w]+)/$",views.UserPosts.as_view(),name="for_user"),
    url(r"by/(?P<username>[-\w]+)/(?P<pk>\d+)/$",views.PostDetail.as_view(),name="single"),
    url(r"delete/(?P<pk>\d+)/$",views.DeletePost.as_view(),name="delete"),
]
