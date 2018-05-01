from django.core.management.base import BaseCommand, CommandError
from pathlib import Path

class Command(BaseCommand):
    help = 'Creates a PostgreSQL COPY statement using the header row of the parcel .csv file'

    def handle(self, *args, **options):
        home = str(Path.home())
        file = home + "/rows.csv"
        try:
            with open(file) as f:
                headers = f.readline()
                split_headers = headers.strip().split(",")
                print(split_headers)
        except Exception as ex:
            print(ex)

