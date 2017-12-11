from rest_framework import generics

from reserve.models import Reservation
from reserve.serializers import ReservationSerializer


class ReservationList(generics.ListCreateAPIView):
    model = Reservation
    queryset = model.objects.all()
    serializer_class = ReservationSerializer


class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Reservation
    queryset = model.objects.all()
    serializer_class = ReservationSerializer
