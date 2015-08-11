import gislite
from osgeo import gdalconst
print(dir(gdalconst))

dataset = gislite.landsat7ds

band = dataset.GetRasterBand(1)
print(band.DataType)

print(gdalconst.GPI_CMYK)
print(gdalconst.GPI_Gray)
print(gdalconst.GPI_HLS)
print(gdalconst.GPI_RGB)

print(gdalconst.GDT_Byte)