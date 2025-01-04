from django.db import models

# Create your models here.

class studentModel(models.Model):
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=150)
    lattitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    route_id = models.CharField(max_length=10)
    student_id = models.IntegerField()

    def __str__(self):
        return self.name