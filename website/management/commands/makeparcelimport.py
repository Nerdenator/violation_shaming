from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Creates a PostgreSQL COPY statement using the header row of the parcel .csv file'

    def handle(self, *args, **options):
