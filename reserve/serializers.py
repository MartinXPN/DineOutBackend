from rest_framework import serializers

from places.serializers import BranchSerializer
from reserve.models import Reservation


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = '__all__'
