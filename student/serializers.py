from rest_framework import serializers

from .models import studentModel

class StudentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = studentModel
        fields = ('name', 'address', 'lattitude', 'longitude', 'route_id',  'student_id')