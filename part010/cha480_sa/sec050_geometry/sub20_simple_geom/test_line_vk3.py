import os
from osgeo import ogr
import shapely
import shapely.geometry

from shapely.ops import cascaded_union

driver = ogr.GetDriverByName('ESRI Shapefile')
out_shp = '/opt/gdata/tmp_demo_data.shp'
if os.path.exists(out_shp):
    driver.DeleteDataSource(out_shp)

newds = driver.CreateDataSource(out_shp)
layernew = newds.CreateLayer('rect',None,ogr.wkbPolygon)

ds = ogr.Open('/opt/gdata/caiyang_route.shp')

layer = ds.GetLayer(0)
feat = layer.GetNextFeature()
while feat:
    geom = feat.GetGeometryRef()
    pts = geom.GetGeometryCount()
    for ii in range(pts):
        poly = geom.GetGeometryRef(ii)
        points_num = poly.GetPointCount()
        print(points_num)
        zc_points = poly.GetPoints()
        print(type(zc_points))
        tmp_pt_arr =  []
        for x in zc_points:
            tmp_pt_arr.append(x)
        pt = shapely.geometry.LineString(tmp_pt_arr)
        vv = pt.buffer(3000.0)
        new_feat = ogr.Feature(layernew.GetLayerDefn())
        tmp_wkb = vv.to_wkb()
        new_geom = ogr.CreateGeometryFromWkb(tmp_wkb)
        new_feat.SetGeometry(new_geom)
        layernew.CreateFeature(new_feat)
    
    feat = layer.GetNextFeature()


newds.Destroy()
