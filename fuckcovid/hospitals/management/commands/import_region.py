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
                hospital, created = Hospital.objects.get_or_create(
                    region = region,
                    phone = row[0],
                    name = row[1],
                    city = row[2],
                    address = row[3],
                )
                cnt += 1

        self.stdout.write(self.style.SUCCESS(f"Importados con éxito {cnt} hospitales en {region}"))
