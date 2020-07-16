from django.urls import path

from . import views

app_name = 'photography'

print("PHOTO")

urlpatterns = [
    # path('fashion', views.FashionPhotos.as_view(), name="fashion"),
    # path('beauty', views.BeautyPhotos.as_view(), name="beauty"),
    # path('portraits', views.PortraitPhotos.as_view(), name="portraits"),
    # path('kids', views.KidsPhotos.as_view(), name="kids"),
    # path('theater', views.TheaterPhotos.as_view(), name="theater"),
    # path('food', views.FoodPhotos.as_view(), name="food"),
    path('photos_all', views.AllPhotos.as_view(), name="photos_all"),

]
