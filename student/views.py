from rest_framework import viewsets

from .serializers import StudentSerializer
from .models import studentModel

class studentViewSet(viewsets.ModelViewSet):
    queryset = studentModel.objects.all()

    serializer_class = StudentSerializer
