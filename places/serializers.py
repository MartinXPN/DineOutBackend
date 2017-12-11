from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from places.models import Place, PlaceBranch, Image, Service, Address, PlaceInfo


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = ('id',)


class PlaceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceInfo
        exclude = ('id',)


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        exclude = ('id',)


class BranchSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    services = ServiceSerializer(many=True)
    place_info = PlaceInfoSerializer(many=True)

    class Meta:
        model = PlaceBranch
        fields = '__all__'


class PlaceSerializer(serializers.ModelSerializer):
    branches = BranchSerializer(many=True)

    class Meta:
        model = Place
        fields = '__all__'
