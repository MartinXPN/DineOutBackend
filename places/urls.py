from django.urls import path

from places.views import PlacesList, PlaceDetail


urlpatterns = [
    path('', PlacesList.as_view(), name='places'),
    path('<pk>', PlaceDetail.as_view(), name='place-details'),
]
