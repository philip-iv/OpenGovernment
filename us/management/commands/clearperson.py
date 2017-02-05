from django.core.management.base import BaseCommand
from us.models import Person

class Command(BaseCommand):
    def handle(self, *args, **options):
        Person.objects.all().delete()