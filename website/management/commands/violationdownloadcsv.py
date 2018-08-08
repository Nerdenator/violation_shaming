from django.core.management.base import BaseCommand, CommandError
from subprocess import call
from pathlib import Path


class Command(BaseCommand):
    help = 'Pulls latest version of the .csv file for the violation data set from OpenData KC.'

    def handle(self, *args, **options):
        home = str(Path.home())
        try:
            call(["wget", "https://data.kcmo.org/api/views/nhtf-e75a/rows.csv", "--directory-prefix=" + home,
                  '-O' + " violation.csv"])
        except Exception:
            raise CommandError("Can't get the data. Try again later. Or, you know... don't.")
