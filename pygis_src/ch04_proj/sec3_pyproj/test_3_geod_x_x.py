#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from pyproj import Geod
g=Geod(ellps='krass')
###############################################################################
miniearth=Geod(a=2,b=1.97)
###############################################################################
###############################################################################
###############################################################################
g = Geod(ellps='clrk66') # Use Clarke 1966 ellipsoid.
# specify the lat/lons of some cities.
boston_lat = 42.+(15./60.); boston_lon = -71.-(7./60.)
portland_lat = 45.+(31./60.); portland_lon = -123.-(41./60.)
newyork_lat = 40.+(47./60.); newyork_lon = -73.-(58./60.)
london_lat = 51.+(32./60.); london_lon = -(5./60.)
# compute forward and back azimuths, plus distance
# between Boston and Portland.
az12,az21,dist = g.inv(boston_lon,boston_lat,portland_lon,portland_lat)
print ("%7.3f %6.3f %12.3f" % (az12,az21,dist))
# compute latitude, longitude and back azimuth of Portland,
# given Boston lat/lon, forward azimuth and distance to Portland.
endlon, endlat, backaz = g.fwd(boston_lon,boston_lat, az12, dist)
print("%6.3f  %6.3f %13.3f" % (endlat,endlon,backaz))
# compute the azimuths, distances from New York to several
# cities (pass a list)
lons1 = 3*[newyork_lon]; lats1 = 3*[newyork_lat]
lons2 = [boston_lon, portland_lon, london_lon]
lats2 = [boston_lat, portland_lat, london_lat]
az12,az21,dist = g.inv(lons1,lats1,lons2,lats2)
for faz,baz,d in zip(az12,az21,dist): print("%7.3f %7.3f %9.3f" % (faz,baz,d))

###############################################################################
###############################################################################
g = Geod(ellps='clrk66')
###############################################################################
boston_lat = 42.+(15./60.); boston_lon = -71.-(7./60.)
portland_lat = 45.+(31./60.); portland_lon = -123.-(41./60.)
###############################################################################
lonlats = g.npts(boston_lon,boston_lat,portland_lon,portland_lat,10)
for lon,lat in lonlats: print('%6.3f  %7.3f' % (lat, lon))

