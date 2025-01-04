from django.db import models

# Create your models here.

class routeModel(models.Model):
    route_id = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    
    def __str__(self):
        return str(self.route_id)