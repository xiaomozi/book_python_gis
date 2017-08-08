# -*- coding:utf-8 -*-
from osgeo import ogr
import os,math
driver = ogr.GetDriverByName("ESRI Shapefile")


extfile = 'rect_field_demo.shp'
if os.access( extfile, os.F_OK ):
    driver.DeleteDataSource( extfile )

extent = [400, 1100, 300, 600]

newds = driver.CreateDataSource(extfile)
layernew = newds.CreateLayer('rect',None,ogr.wkbPolygon)

fieldcnstr = ogr.FieldDefn("fd",ogr.OFTString)
fieldcnstr.SetWidth(32)
layernew.CreateField(fieldcnstr)
fieldf = ogr.FieldDefn("f",ogr.OFTReal)
layernew.CreateField(fieldf)

wkt = 'POLYGON ((%f %f,%f %f,%f %f,%f %f,%f %f))' % (extent[0],extent[3],
    extent[1],extent[3], extent[1],extent[2],
    extent[0],extent[2], extent[0],extent[3])


geom = ogr.CreateGeometryFromWkt(wkt)
feat = ogr.Feature(layernew.GetLayerDefn())
feat.SetField('fd',"这里是字段的值")# 测试中文字段名和字段值
feat.SetGeometry(geom)
layernew.CreateFeature(feat)
newds.Destroy()

