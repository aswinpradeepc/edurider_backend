from django.core.management.base import BaseCommand
from student.models import studentModel  # Replace with actual app name
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Populate 30 random student records'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Clear existing records (optional)
        studentModel.objects.all().delete()

        # Generate 30 records
        for _ in range(100):
            student = studentModel.objects.create(
                name=fake.name(),
                address=fake.address(),
                lattitude=round(fake.latitude(), 6),
                longitude=round(fake.longitude(), 6),
                route_id=f'RT-{random.randint(100, 999)}',
                student_id=random.randint(10000, 99999)
            )
            student.save()

        self.stdout.write(self.style.SUCCESS('Successfully created student records'))
