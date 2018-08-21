from django.db import models, connection


class Parcel(models.Model):
    objectid = models.TextField(null=True, blank=True)
    parcelid = models.TextField(null=True, blank=True)
    kivapin = models.TextField(unique=True, default="0", null=False)
    address = models.TextField(null=True, blank=True)
    subdivision = models.TextField(null=True, blank=True)
    block = models.TextField(null=True, blank=True)
    lot = models.TextField(null=True, blank=True)
    datecreated = models.TextField(null=True, blank=True)
    landusecode = models.TextField(null=True, blank=True)
    apn = models.TextField(null=True, blank=True)
    parceltype = models.TextField(null=True, blank=True)
    status = models.TextField(null=True, blank=True)
    condo = models.TextField(null=True, blank=True)
    platname = models.TextField(null=True, blank=True)
    fraction = models.TextField(null=True, blank=True)
    prefix = models.TextField(null=True, blank=True)
    suite = models.TextField(null=True, blank=True)
    own_name = models.TextField(null=True, blank=True)
    own_addr = models.TextField(null=True, blank=True)
    own_city = models.TextField(null=True, blank=True)
    own_state = models.TextField(null=True, blank=True)
    own_zip = models.TextField(null=True, blank=True)
    blvdfront = models.TextField(null=True, blank=True)
    lastupdate = models.TextField(null=True, blank=True)
    shape_length = models.TextField(null=True, blank=True)
    shape_area = models.TextField(null=True, blank=True)
    latitude = models.TextField(null=True, blank=True)
    longitude = models.TextField(null=True, blank=True)
    location1 = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.own_name

class Violation(models.Model):
    propertyviolationid = models.TextField(null=True, blank=True)
    caseid = models.TextField(null=True, blank=True)
    status = models.TextField(null=True, blank=True)
    caseopeneddate = models.TextField(null=True, blank=True)
    casecloseddate = models.TextField(null=True, blank=True)
    daysopen = models.TextField(null=True, blank=True)
    violationcode = models.TextField(null=True, blank=True)
    violationdescription = models.TextField(null=True, blank=True)
    ordinancenumber = models.TextField(null=True, blank=True)
    ordinancechapter = models.TextField(null=True, blank=True)
    violationentrydate = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    county = models.TextField(null=True, blank=True)
    state = models.TextField(null=True, blank=True)
    zipcode = models.TextField(null=True, blank=True)
    latitude = models.TextField(null=True, blank=True)
    longitude = models.TextField(null=True, blank=True)
    kivapin = models.ForeignKey(Parcel, to_field="kivapin", on_delete=models.CASCADE)
    councildistrict = models.TextField(null=True, blank=True)
    policepatrolarea = models.TextField(null=True, blank=True)
    inspectionarea = models.TextField(null=True, blank=True)
    neighborhood = models.TextField(null=True, blank=True)
    codeviolationlocation = models.TextField(null=True, blank=True)


class ViolationStaging(models.Model):
    """
    The purpose of this table is to create a table that can be narrowed down to fit the
    constraints of Violation table. Violation needs a non-0 kivapin.
    """
    propertyviolationid = models.TextField(null=True, blank=True)
    caseid = models.TextField(null=True, blank=True)
    status = models.TextField(null=True, blank=True)
    caseopeneddate = models.TextField(null=True, blank=True)
    casecloseddate = models.TextField(null=True, blank=True)
    daysopen = models.TextField(null=True, blank=True)
    violationcode = models.TextField(null=True, blank=True)
    violationdescription = models.TextField(null=True, blank=True)
    ordinancenumber = models.TextField(null=True, blank=True)
    ordinancechapter = models.TextField(null=True, blank=True)
    violationentrydate = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    county = models.TextField(null=True, blank=True)
    state = models.TextField(null=True, blank=True)
    zipcode = models.TextField(null=True, blank=True)
    latitude = models.TextField(null=True, blank=True)
    longitude = models.TextField(null=True, blank=True)
    kivapin = models.TextField(null=True, blank=True)
    councildistrict = models.TextField(null=True, blank=True)
    policepatrolarea = models.TextField(null=True, blank=True)
    inspectionarea = models.TextField(null=True, blank=True)
    neighborhood = models.TextField(null=True, blank=True)
    codeviolationlocation = models.TextField(null=True, blank=True)

# def violations_per_county():
#     county_count = {counted: Violation.objects.filter(county=counted).count() for counted in
#                     ('Platte', 'Clay', 'Cass', 'Jackson')}
#     return county_count
#

# def get_top_ten_violators():
#     with connection.cursor() as cursor:
#         cursor.execute(
#             "SELECT p.own_name FROM website_parcel p INNER JOIN website_violation v ON p.kivapin = v.kivapin")
#         return cursor.fetchall()

def top_10_violating_properties_jackson():
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT website_violation.address, count(website_violation.address) "
            "AS address_count, website_parcel.own_name, website_parcel.own_city, website_parcel.own_state "
            "FROM website_violation "
            "INNER JOIN website_parcel "
            "ON website_parcel.kivapin = website_violation.kivapin "
            "WHERE website_violation.county = 'Jackson' "
            "AND website_violation.status = 'Open' "
            "GROUP BY website_violation.address, website_parcel.own_name, website_parcel.own_city, website_parcel.own_state "
            "ORDER BY address_count DESC"
        )
        results = cursor.fetchall()
        return results


def top_10_violating_owners_jackson():
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT count(website_violation.address) AS address_count, website_parcel.own_name, website_parcel.own_city, website_parcel.own_state "
            "FROM website_parcel "
            "INNER JOIN website_violation "
            "ON website_violation.kivapin = website_parcel.kivapin "
            "WHERE website_violation.county = 'Jackson' "
            "AND website_violation.status = 'Open' "
            "GROUP BY website_parcel.own_name, website_parcel.own_city, website_parcel.own_state "
            "ORDER BY address_count DESC "
            "LIMIT 10;")
        results = cursor.fetchall()
        return results
