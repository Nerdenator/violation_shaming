from django.shortcuts import render
from website.models import Violation


def basic_county_data(request):
    county_count = {counted: Violation.objects.filter(county=counted).filter(status='Open').count() for counted in
                    ('Platte', 'Clay', 'Cass', 'Jackson')}
    jackson_violations = Violation.objects.filter(county="Jackson").filter(status='Open')
    return render(request, 'website/index.html', {'violations_per_county': county_count})
