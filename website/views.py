from django.shortcuts import render
from website.models import Violation


# get list of counties with violations, ranked.
def counties_with_violation_count(request):
    # gets the Django ORM count for the violations in each county
    county_count = {counted: Violation.objects.filter(county=counted).count() for counted in
                    ('Platte', 'Clay', 'Cass', 'Jackson')}
    return render(request, 'website/index.html', { 'violations_per_county': county_count })