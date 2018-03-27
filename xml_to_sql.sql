<!-- from https://stackoverflow.com/questions/19007884/import-xml-files-to-postgresql-->
SELECT
  (xpath('//objectid/text()', myTempTable.myXmlColumn))[1]::text AS objectid,
  (xpath('//parcelid/text()', myTempTable.myXmlColumn))[1]::text AS parcelid,
  (xpath('//kivapin/text()', myTempTable.myXmlColumn))[1]::text AS kivapin,
  (xpath('//subdivision/text()', myTempTable.myXmlColumn))[1]::text AS subdivision,
  (xpath('//block/text()', myTempTable.myXmlColumn))[1]::text AS block,
  (xpath('//lot/text()', myTempTable.myXmlColumn))[1]::text AS lot,
  (xpath('//datecreated/text()', myTempTable.myXmlColumn))[1]::text AS datecreated,
  (xpath('//landusecode/text()', myTempTable.myXmlColumn))[1]::text AS landusecode,
  (xpath('//apn/text()', myTempTable.myXmlColumn))[1]::text AS apn,
  (xpath('//parceltype/text()', myTempTable.myXmlColumn))[1]::text AS parceltype,
  (xpath('//status/text()', myTempTable.myXmlColumn))[1]::text AS status,
  (xpath('//condo/text()', myTempTable.myXmlColumn))[1]::text AS condo,
  (xpath('//platname/text()', myTempTable.myXmlColumn))[1]::text AS platname,
  (xpath('//fraction/text()', myTempTable.myXmlColumn))[1]::text AS fraction,
  (xpath('//prefix/text()', myTempTable.myXmlColumn))[1]::text AS prefix,
  (xpath('//suite/text()', myTempTable.myXmlColumn))[1]::text AS suite,
  (xpath('//own_name/text()', myTempTable.myXmlColumn))[1]::text AS own_name,
  (xpath('//own_addr/text()', myTempTable.myXmlColumn))[1]::text AS own_addr,
  (xpath('//own_city/text()', myTempTable.myXmlColumn))[1]::text AS own_city,
  (xpath('//own_zip/text()', myTempTable.myXmlColumn))[1]::text AS own_zip,
  (xpath('//blvdfront/text()', myTempTable.myXmlColumn))[1]::text AS blvdfront,
  (xpath('//lastupdate/text()', myTempTable.myXmlColumn))[1]::text AS lastupdate,
  (xpath('//shape_length/text()', myTempTable.myXmlColumn))[1]::text AS shape_length,
  (xpath('//shape_area/text()', myTempTable.myXmlColumn))[1]::text AS shape_area,
  (xpath('//latitude/text()', myTempTable.myXmlColumn))[1]::text AS latitude,
  (xpath('//longitude/text()', myTempTable.myXmlColumn))[1]::text AS longitude,
  (xpath('//location1/text()' myTempTable.myXmlColumn))[1]::text AS location1,
  myTempTable.myXmlColumn as myXmlElement
FROM unnest(
  '//row'
  ,XMLPARSE(DOCUMENT convert_from(pg_read_binary_file('parcel_data_first_row.xml'), 'UTF8'))
) AS myTempTable(myXmlColumn);
