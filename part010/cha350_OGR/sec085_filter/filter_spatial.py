import os
from osgeo import ogr
def create_shp_by_layer(shp, layer):
    outputfile = shp
    if os.access(outputfile, os.F_OK):
        driver.DeleteDataSource(outputfile)
    newds = driver. CreateDataSource ( outputfile )
    pt_layer = newds.CopyLayer ( layer, '')
    newds.Destroy ()
driver = ogr.GetDriverByName("ESRI Shapefile")
world_shp = '/opt/gdata/fenxian.shp'
cover_shp = '/opt/gdata/sel.shp'
world_ds = ogr.Open(world_shp)
cover_ds = ogr.Open(cover_shp)
world_layer = world_ds.GetLayer(0)
cover_layer = cover_ds.GetLayer(0)
print(world_layer.GetFeatureCount())
cover_feats = cover_layer.GetNextFeature()

poly = cover_feats.GetGeometryRef()
world_layer.SetSpatialFilter(poly)
print(type(world_layer))
out_shp = '/opt/gdata/sel_res.shp'
create_shp_by_layer(out_shp, world_layer)