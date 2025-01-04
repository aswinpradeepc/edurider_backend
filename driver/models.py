from django.db import models
from routes.models import routeModel

# Create your models here.

class driverModel(models.Model):
    name = models.CharField(max_length=60)
    driver_id = models.IntegerField(unique=True)
    route_id = models.ForeignKey(routeModel, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name