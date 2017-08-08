import sys
from osgeo import ogr
inshp = '/bk/gdata/world_borders.shp'
driver = ogr.GetDriverByName('ESRI Shapefile')
dataSource = driver.Open(inshp,0)
if dataSource is None:
    print 'could not open'
    sys.exit(1)
print 'done!'
