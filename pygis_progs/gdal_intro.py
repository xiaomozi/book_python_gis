import gislite
try :
    import gdal
except:
    from osgeo import gdal

from osgeo.gdalconst import *
gdal.AllRegister()
driver = gdal.GetDriverByName('GeoTiff')
print(driver == None)

driver2 = gdal.GetDriverByName('GTiff')
print(driver2 == None)
print(dir(driver2))
print(driver2.thisown)



drv_count = gdal.GetDriverCount()
for idx in range(drv_count):
    driver = gdal.GetDriver(idx)
    print ( "%10s: %s" % (driver.ShortName, driver.LongName))

landtif = gislite.tif_landsat7

dataset = gdal.Open(landtif)
print(dir(dataset))
print(dataset.GetDescription())
print(dataset.RasterCount)
img_width, img_height = dataset.RasterXSize, dataset.RasterYSize
print(img_width, img_height)
print(dataset.GetGeoTransform())
print(dataset.GetProjection())

print(dataset.GetMetadata())