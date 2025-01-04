from rest_framework import viewsets

from .serializers import DriverSerializer
from .models import driverModel

class driverViewSet(viewsets.ModelViewSet):
    queryset = driverModel.objects.all()

    serializer_class = DriverSerializer
