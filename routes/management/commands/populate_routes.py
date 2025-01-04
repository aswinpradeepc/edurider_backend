from django.core.management.base import BaseCommand
from routes.models import routeModel  # Replace with actual app name
from faker import Faker
import random

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Clear existing records (optional)
        routeModel.objects.all().delete()

        for _ in range(10):
            routes = routeModel.objects.create(
                route_id = random.randint(10000, 99999),
                capacity = 50
            )
            routes.save()

        self.stdout.write(self.style.SUCCESS('Successfully created 10 routes'))
