from rest_framework import serializers

from .models import driverModel

class DriverSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = driverModel
        fields = ('name', 'driver_id', 'route_id')