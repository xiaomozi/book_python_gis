import os
from osgeo import ogr
import shapely
import shapely.geometry


driver = ogr.GetDriverByName('ESRI Shapefile')
out_shp = '/opt/gdata/tmp_demo_data.shp'
if os.path.exists(out_shp):
    driver.DeleteDataSource(out_shp)

newds = driver.CreateDataSource(out_shp)
layernew = newds.CreateLayer('rect',None,ogr.wkbPolygon)

ds = ogr.Open('/opt/gdata/burkitt.shp')

layer = ds.GetLayer(0)
feat = layer.GetNextFeature()
while feat:
    fid = feat.GetField('X') 
    print(fid)
    geom = feat.GetGeometryRef()
    # print(geom.geom_type)
    print(geom)
    pt = shapely.geometry.Point(geom.GetX(), geom.GetY())
    vv = pt.buffer(3.0)
    # print(vv)
    # print(type(vv))

    tmp_wkb = vv.to_wkb()

    new_geom = ogr.CreateGeometryFromWkb(tmp_wkb)
    new_feat = ogr.Feature(layernew.GetLayerDefn())
    new_feat.SetGeometry(new_geom)
    layernew.CreateFeature(new_feat)

    feat = layer.GetNextFeature()


newds.Destroy()
