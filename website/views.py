from django.shortcuts import render
from website.models import Violation
from django.db import connection

def basic_county_data(request):
    county_count = {counted: Violation.objects.filter(county=counted).filter(status='Open').count() for counted in
                    ('Platte', 'Clay', 'Cass', 'Jackson')}


    return render(request, 'website/index.html', {'violations_per_county': county_count})


def custom_sql_get_top_10_jackson(self):
    with connection.cursor() as cursor:
        cursor.execute()