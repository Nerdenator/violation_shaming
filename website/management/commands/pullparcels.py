from django.core.management.base import BaseCommand, CommandError
from subprocess import call

class Command(BaseCommand):
    help = 'Pulls latest version of the .csv file for the parcels data set from OpenData KC.'

    def handle(self, *args, **options):
        try:
            call(["wget", "https://data.kcmo.org/api/views/vrys-qgrz/rows.csv"])
        except Exception:
            raise CommandError("Can't get the data. Try again later. Or, you know... don't.")