import struct
from osgeo import ogr
from array import array

import sys
endian_name = sys.byteorder

wkbXDR = '>'     # Big Endian
wkbNDR = '<'     # Little Endian

def choose(bool, a, b):
    return (bool and [a] or [b])[0]

BTOR = choose(endian_name == 'little',wkbNDR,wkbNDR)

def up_endian_type(wkb):
    endian_t = struct.unpack('b',wkb[0])[0]
    endian = choose(endian_t,'<','>')
    wkbtype = struct.unpack(endian+'I',wkb[1:5])[0]
    return endian,wkbtype,endian_t

def up_len(wkb,beg,endian):
    return struct.unpack(endian+'I',wkb[beg:beg+4])[0]

def up_point(wkb):
    endian,wkbtype,et = up_endian_type(wkb)
    points = struct.unpack(endian+"2d",wkb[5:])
    return points

def up_linestring(wkb):
    endian,wkbtype,et = up_endian_type(wkb)
    lenght = up_len(wkb,5,endian)
    points = array('d',wkb[9:9+lenght*16])
    if endian != BTOR : points.byteswap()
    return points

def up_linearring(wkb,ringcount,endian):
    #endian,wkbtype,et = up_endian_type(wkb)
    points = []
    ptr = 0
    for i in range(ringcount):
        length = up_len(wkb,ptr,endian)
        ps = array('d',wkb[ptr+4:ptr+4+length*16])
        if endian != BTOR : ps.byteswap()
        points.append(ps)
        ptr += 4+length*16
    return points,ptr

def up_polygon(wkb,sub=-1):
    if sub == -1:
        ringcount = up_len(wkb,5,endian)
        points = up_linearring(wkb[9:],ringcount,endian)[0]
        return points
    else:
        points = []
        ptr = 5
        ringcount = up_len(wkb,ptr,endian)
        ps,ringlen = up_linearring(wkb[ptr+4:],ringcount,endian)
        points.append(ps)
        ptr += 4+ringlen
        return points,ptr

def up_mpoint(wkb):
    endian,wkbtype,et = up_endian_type(wkb)
    subcount = up_len(wkb,5,endian)
    points = []
    ptr = 9
    for i in range(subcount):
        subps = up_point(wkb[ptr:])
        points.append(subps)
        ptr += 9+len(subps)*8
    return points

def up_mlinestring(wkb):
    endian,wkbtype,et = up_endian_type(wkb)
    subcount = up_len(wkb,5,endian)
    points = []
    ptr = 9
    for i in range(subcount):
        subps = up_linestring(wkb[ptr:])
        points.append(subps)
        ptr += 9+len(subps)*8
    return points

def up_mpolygon(wkb):
    endian,wkbtype,et = up_endian_type(wkb)
    subcount = up_len(wkb,5,endian)
    points = []
    ptr = 9
    for i in range(subcount):
        subps,size = up_polygon(wkb[ptr:],i)
        points.append(subps)
        ptr += size
    return points

fun_map = {
        ogr.wkbPoint : up_point,
        ogr.wkbLineString : up_linestring,
        ogr.wkbPolygon : up_polygon,
        ogr.wkbMultiPoint : up_mpoint,
        ogr.wkbMultiLineString : up_mlinestring,
        ogr.wkbMultiPolygon : up_mpolygon
        }

def WkbUnPacker(wkb):
    endian,wkbtype,endian_t = up_endian_type(wkb)
    foo = fun_map[wkbtype]
    points = foo(wkb)
    return [endian_t,wkbtype,points]


if __name__ == "__main__":
    import time
    ds = ogr.Open("/gdata/world_borders.shp")
    layer = ds.GetLayer()
    begt = time.time()
    #count = layer.GetFeatureCount()
    #count  = 2
    feature = layer.GetNextFeature()
    #for i in [1]:#range(count):
    while feature is not None:
        #feature = layer.GetFeature(i)
        geom = feature.GetGeometryRef()
        # print geom.ExportToWkt()
        wkb = geom.ExportToWkb()
        wkbarr = WkbUnPacker(wkb)
        feature = layer.GetNextFeature()
        #print wkbarr
    print time.time()-begt
