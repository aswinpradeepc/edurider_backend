from rest_framework import viewsets

from .serializers import RouteSerializer
from .models import routeModel

class routeViewSet(viewsets.ModelViewSet):
    queryset = routeModel.objects.all()
    
    serializer_class = RouteSerializer