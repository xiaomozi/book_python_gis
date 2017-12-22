#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################


###############################################################################
from osgeo import gdal
dataset = gdal.Open('/gdata/lu75i1.tif')
band = dataset.GetRasterBand(1)
band.GetRasterColorInterpretation()
###############################################################################
from osgeo import gdalconst
gdalconst.GCI_PaletteIndex
colormap = band.GetRasterColorTable()
dir(colormap)
colormap.GetCount()
colormap.GetPaletteInterpretation()
gdalconst.GPI_RGB
###############################################################################
for i in range(colormap.GetCount()):
    print("%i:%s" % (i, colormap.GetColorEntry(i)))

###############################################################################
from osgeo import gdalconst
dir(gdalconst)
gdalconst.GPI_CMYK
gdalconst.GPI_Gray
gdalconst.GPI_HLS
gdalconst.GPI_RGB
gdalconst.GDT_Byte
