from django.urls import path

from places.views import PlacesList, PlaceDetail, BranchDetail, BranchList

urlpatterns = [
    path('', PlacesList.as_view()),
    path('<pk>', PlaceDetail.as_view()),
    path('branches', BranchList.as_view()),
    path('branches/<pk>', BranchDetail.as_view()),
]
