from django.shortcuts import render
from website.models import Violation


# get list of counties with violations, ranked.
def counties_with_violation_count():
    counties = {'Clay': None, 'Cass': None, 'Jackson': None, 'Platte': None}
    # convert ^this^ to key-val pairs. for each county, run
    # Violation.objects.filter(county=county).count() and
    # and assign the resulting result set to the value in the pair.
    # pretty damned proud of this
    county_count = {counted: Violation.objects.filter(county=counted).count() for counted in
                    ('Platte', 'Clay', 'Cass', 'Jackson')}