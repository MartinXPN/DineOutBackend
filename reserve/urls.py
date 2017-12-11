from django.urls import path

from reserve.views import ReservationList, ReservationDetail

urlpatterns = [
    path('', ReservationList.as_view()),
    path('<pk>', ReservationDetail.as_view()),
]
