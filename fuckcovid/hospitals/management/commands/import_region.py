import csv
from django.core.management.base import BaseCommand, CommandError
from fuckcovid.hospitals.models import Region, Hospital

class Command(BaseCommand):
    help = 'Importa los datos de los hospitales de una región'

    def add_arguments(self, parser):
        parser.add_argument('region')
        parser.add_argument('file')

    def handle(self, *args, **options):
        region, created = Region.objects.get_or_create(name=options['region'])

        cnt = 0
        with open(options['file']) as f:
            reader = csv.reader(f)
            for row in reader:
                try:
                    phone = row[0]
                except IndexError:
                    phone = ''
                try:
                    name = row[1]
                except IndexError:
                    name = ''
                try:
                    city = row[2]
                except IndexError:
                    city = ''
                try:
                    address = row[3]
                except IndexError:
                    address = ''
                hospital, created = Hospital.objects.get_or_create(
                    region = region,
                    phone = phone,
                    name = name,
                    city = city,
                    address = address,
                )
                cnt += 1

        self.stdout.write(self.style.SUCCESS(f"Importados con éxito {cnt} hospitales en {region}"))
