COPY website_violation(property_violation_id,
case_id,
status,
case_opened,
case_closed,
days_open,
violation_code,
violation_description,
ordinance_number,
ordinance_chapter,
violation_entry_date,
address,
county,
state,
zip_code,
latitude,
longitude,
kiva_pin,
council_district,
police_patrol,
inspection_area,
neighborhood,
code_violation_location) from '/home/aaron/property_violations.csv' DELIMITER ',' CSV HEADER;
