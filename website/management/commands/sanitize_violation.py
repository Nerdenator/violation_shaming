from django.core.management.base import BaseCommand, CommandError
from pathlib import Path
from django.db import connection


class Command(BaseCommand):
    help = 'Creates a table filled with Violation csv, then sanitizes it for import to Violation table.'

    def handle(self, *args, **options):
        home = str(Path.home())
        print(home)
        file = home + "/violation.csv"
        try:
            with open(file) as f:
                print("thing")
                headers = f.readline()
                split_headers = headers.replace(" ", "").split(",")
                print(split_headers)
                myString = ", ".join(split_headers)
                query = "COPY website_violation(" + myString + ") from '" + file + "' DELIMITER ',' CSV HEADER;"
                with connection.cursor() as cursor:
                    cursor.execute(query)

        except Exception as ex:
            print(ex)
