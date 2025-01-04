from rest_framework import serializers

from .models import routeModel

class RouteSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = routeModel
        fields = ('route_id', 'capacity')
        