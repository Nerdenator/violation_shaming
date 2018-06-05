from django.shortcuts import render
from website.models import Violation, top_10_violating_properties_jackson, top_10_violating_owners_jackson
from django.db import connection


def basic_county_data(request):
    county_count = {counted: Violation.objects.filter(county=counted).filter(status='Open').count() for counted in
                    ('Platte', 'Clay', 'Cass', 'Jackson')}
    jackson_properties = top_10_violating_properties_jackson()
    jackson_owners = top_10_violating_owners_jackson()
    return render(request, 'website/index.html',
                  {'violations_per_county': county_count, 'jackson_top_10_properties': jackson_properties,
                   'jackson_top_10_owners': jackson_owners})
