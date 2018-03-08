from django.db import models


# Create your models here.
class Parcel(models.Model):
    objectid = models.IntegerField(null=True, blank=True)
    parcelid = models.IntegerField(null=True, blank=True)
    kivapin = models.TextField()
    subdivision = models.CharField(max_length=200)
    block = models.IntegerField(null=True, blank=True)
    lot = models.CharField(max_length=10)
    datecreated = models.DateField(null=True, blank=True)
    landusecode = models.CharField(max_length=500)
    apn = models.CharField(max_length=100)
    parceltype = models.CharField(max_length=20)
    status = models.CharField(max_length=50)
    condo = models.CharField(max_length=10)
    platname = models.CharField(max_length=200)
    fraction = models.CharField(max_length=10)
    prefix = models.CharField(max_length=10)
    suite = models.CharField(max_length=20)
    own_name = models.CharField(max_length=500)
    own_addr = models.CharField(max_length=500)
    own_city = models.CharField(max_length=100)
    own_zip = models.CharField(max_length=20)
    blvdfront = models.IntegerField(null=True, blank=True)
    lastupdate = models.DateField(null=True, blank=True)
    shape_length = models.FloatField()
    shape_area = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    location1 = models.CharField(max_length=500)


class Violation(models.Model):
    property_violation_id = models.IntegerField(default=0)
    case_id = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=20, default='')
    case_opened = models.DateField(null=True, blank=True)
    case_closed = models.DateField(null=True, blank=True)
    days_open = models.IntegerField(default=0)
    violation_code = models.CharField(max_length=50, default='')
    violation_description = models.CharField(max_length=200, default='')
    ordinance_number = models.CharField(max_length=20, default='')
    ordinance_chapter = models.IntegerField(default=0)
    violation_entry_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=100, default='')
    county = models.CharField(max_length=20, default='')
    state = models.CharField(max_length=4, default='')
    zip_code = models.CharField(max_length=20, default='')
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    kiva_pin = models.IntegerField(default=0)
    council_district = models.IntegerField(default='')
    police_patrol = models.CharField(max_length=20, default='')
    inspection_area = models.IntegerField(default=0)
    neighborhood = models.CharField(max_length=150, default='')
    code_violation_location = models.CharField(max_length=150, default='')