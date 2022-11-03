alter table avydata3                         --Need to break up coordinates into LAT and LONG for GeoJson
add LATITUDE VARCHAR(255);					--I'll create some new columes to store LAT and LONG in
alter table avydata3
ADD LONGITUDE VARCHAR(255);


UPDATE avydata3								--Breaking up the coordinates column by the "," and placing data in new columns
set latitude = Substring(COORDINATES, 1,Charindex(',', COORDINATES)-1)
UPDATE avydata3
set longitude = Substring(COORDINATES, Charindex(',', COORDINATES)+1, LEN(COORDINATES))
select * from avydata3


