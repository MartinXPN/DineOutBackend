from rest_framework import serializers

from places.models import Place, PlaceBranch


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceBranch
        fields = '__all__'
