from django.core.management.base import BaseCommand
from django.db.models import Q

from mainapp.models import Product

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def filter_hoodi(self):
        return ~Q(name__startswith='Худи') | Q(price__lt=7000)

    def handle(self, *args, **options):
        pr = Product.objects.filter(self.filter_hoodi()).all()
        print(pr)

