SELECT count(*)
FROM website_violation
  INNER JOIN website_parcel
    ON (website_violation.address = website_parcel.own_addr)
WHERE website_violation.county = 'Jackson';

SELECT *
FROM website_parcel
WHERE kivapin IN (SELECT kivapin
                  FROM website_parcel
                  WHERE kivapin IN (
                    SELECT kivapin
                    FROM website_parcel
                    GROUP BY kivapin
                    HAVING COUNT(*) > 1))
ORDER BY kivapin;

SELECT count(*)
FROM website_parcel;

SELECT *
FROM website_parcel
WHERE website_parcel.kivapin IS NULL;

CREATE TABLE jackson_co_open_vio_par AS
  SELECT
    wv.property_violation_id   AS wv_property_violation_id,
    wv.case_id                 AS wv_case_id,
    wv.status                  AS wv_status,
    wv.case_opened             AS wv_case_opened,
    wv.case_opened             AS wv_case_closed,
    wv.days_open               AS wv_days_open,
    wv.violation_code          AS wv_violation_code,
    wv.violation_description   AS wv_violation_description,
    wv.ordinance_number        AS wv_ordinance_number,
    wv.ordinance_chapter       AS wv_ordinance_chapter,
    wv.violation_entry_date    AS wv_violation_entry_date,
    wv.address                 AS wv_address,
    wv.county                  AS wv_county,
    wv.state                   AS wv_state,
    wv.zip_code                AS wv_zip_code,
    wv.latitude                AS wv_latitude,
    wv.longitude               AS wv_longitude,
    wv.council_district        AS wv_council_district,
    wv.police_patrol           AS wv_police_patrol,
    wv.inspection_area         AS wv_inspection_area,
    wv.neighborhood            AS wv_neighborhood,
    wv.code_violation_location AS wv_code_violation_location,
    wv.kivapin                 AS wv_kviapin,
    wp.objectid                AS wp_object_id,
    wp.parcelid                AS wp_parcel_id,
    wp.kivapin                 AS wp_kivapin,
    wp.address                 AS wp_address,
    wp.subdivision             AS wp_subdivision,
    wp.block                   AS wp_block,
    wp.lot                     AS wp_lot,
    wp.datecreated             AS wp_datecreated,
    wp.landusecode             AS wp_landusecode,
    wp.apn                     AS wp_apn,
    wp.parceltype              AS wp_parceltype,
    wp.status                  AS wp_status,
    wp.condo                   AS wp_condo,
    wp.platname                AS wp_platname,
    wp.fraction                AS wp_fraction,
    wp.prefix                  AS wp_prefix,
    wp.suite                   AS wp_suite,
    wp.own_name                AS wp_own_name,
    wp.own_addr                AS wp_own_addr,
    wp.own_city                AS wp_own_city,
    wp.own_zip                 AS wp_own_zip,
    wp.own_state               AS wp_own_state,
    wp.blvdfront               AS wp_blvdfront,
    wp.lastupdate              AS wp_lastupdate,
    wp.shape_length            AS wp_shape_length,
    wp.shape_area              AS wp_shape_area,
    wp.latitude                AS wp_latitude,
    wp.longitude               AS wp_longitude,
    wp.location1               AS wp_location1
  FROM website_violation wv
    INNER JOIN website_parcel wp
      ON (wv.kivapin = wp.kivapin)
         AND wv.county = 'Jackson'
         AND wv.status = 'Open';


select count(DISTINCT violation_description)
FROM website_violation;

SELECT
  county,
  COUNT(county)
FROM website_violation
GROUP BY county;

SELECT
  wv_violation_code,
  count(wv_violation_code)
FROM jackson_co_open_vio_par jc
WHERE jc.wp_own_state = 'MO'
GROUP BY wv_violation_code
ORDER BY count(wv_violation_code) DESC;

SELECT
  wv_address,
  COUNT(wv_address)
FROM jackson_co_open_vio_par jcovp
GROUP BY wv_address
ORDER BY count(wv_address) DESC;

SELECT *
FROM jackson_co_open_vio_par
WHERE wv_address = '2637 MADISON AVE';

SELECT count(*)
FROM jackson_co_open_vio_par
WHERE wv_case_closed IS NOT NULL
AND wv_status = 'Open';

SELECT *
FROM website_violation
WHERE case_closed IS NOT NULL
AND status = 'Open';

SELECT DISTINCT wv_address
FROM jackson_co_open_vio_par
WHERE wv_case_closed IS NOT NULL
AND wv_status = 'Open';

SELECT count(*)
FROM website_violation
WHERE county = 'Jackson'
AND status='Open'
AND case_closed IS NOT NULL;

SELECT
  violation_entry_date,
  case_closed,
  case_opened,
  status
FROM website_violation
WHERE
case_closed IS NOT NULL
AND status != 'Closed';

SELECT *
FROM website_violation
WHERE
  neighborhood;

SELECT *
FROM website_violation
WHERE neighborhood = 'Breen Hills'
AND address::text LIKE '%COLRAIN AVE'
ORDER BY address;

SELECT
 website_violation.address, count(website_violation.address) AS address_count, website_parcel.own_name, website_parcel.own_city, website_parcel.own_state
FROM website_violation
  INNER JOIN website_parcel
  ON website_parcel.kivapin = website_violation.kivapin
WHERE website_violation.county = 'Jackson'
  AND website_violation.status = 'Open'
  AND website_parcel.own_name LIKE '%Raineth%'
GROUP BY website_violation.address, website_parcel.own_name, website_parcel.own_city, website_parcel.own_state
ORDER BY address_count DESC;

SELECT
  count(website_violation.address) AS address_count, website_parcel.own_name, website_parcel.own_city, website_parcel.own_state
FROM website_violation
  INNER JOIN website_parcel
  ON website_parcel.kivapin = website_violation.kivapin
WHERE website_violation.county = 'Jackson'
  AND website_violation.status = 'Open'
  AND website_parcel.own_state != 'MO'
  AND website_parcel.own_state != 'KS'
GROUP BY website_parcel.own_name, website_parcel.own_city, website_parcel.own_state
ORDER BY address_count DESC;

SELECT count(website_violation.address) AS address_count, website_parcel.own_name, website_parcel.own_city, website_parcel.own_state
FROM website_parcel
  INNER JOIN website_violation
  ON website_violation.kivapin = website_parcel.kivapin
WHERE website_violation.county = 'Jackson'
AND website_violation.status = 'Open'
GROUP BY website_parcel.own_name, website_parcel.own_city, website_parcel.own_state
ORDER BY address_count DESC;

SELECT count(website_violation.address) AS address_count, website_parcel.own_name, website_parcel.own_city, website_parcel.own_state
FROM website_parcel
  INNER JOIN website_violation
  ON website_violation.kivapin = website_parcel.kivapin
WHERE website_violation.county = 'Jackson'
AND website_violation.status = 'Open'
  AND website_parcel.own_name LIKE '%Raineth%'
GROUP BY website_parcel.own_name, website_parcel.own_city, website_parcel.own_state
ORDER BY address_count DESC;

SELECT website_violation.address, count(website_violation.address) AS address_count, website_parcel.own_name, website_parcel.address, website_parcel.own_city, website_parcel.own_state
            FROM website_violation
            INNER JOIN website_parcel
            ON website_parcel.kivapin = website_violation.kivapin
            WHERE website_violation.county = 'Jackson'
            AND website_violation.status = 'Open'
            AND website_parcel.own_addr != website_violation.address
            GROUP BY website_violation.address, website_parcel.address, website_parcel.own_name, website_parcel.own_city, website_parcel.own_state
            ORDER BY address_count DESC;

SELECT count(*)
FROM website_parcel
WHERE website_parcel.own_name ILIKE '%Raineth%';