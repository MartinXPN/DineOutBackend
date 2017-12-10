from rest_framework import generics

from places.models import Place, PlaceBranch
from places.serializers import PlaceSerializer, BranchSerializer


class PlacesList(generics.ListCreateAPIView):
    model = Place
    queryset = model.objects.all()
    serializer_class = PlaceSerializer


class PlaceDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Place
    queryset = model.objects.all()
    serializer_class = PlaceSerializer


class BranchList(generics.ListCreateAPIView):
    model = PlaceBranch
    queryset = model.objects.all()
    serializer_class = BranchSerializer


class BranchDetail(generics.RetrieveUpdateDestroyAPIView):
    model = PlaceBranch
    queryset = model.objects.all()
    serializer_class = BranchSerializer
