#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from pprint import pprint
import fiona
c = fiona.open('/gdata/world_borders.shp')
pprint(c.schema)
###############################################################################
rec = next(c)
set(rec.keys()) - set(c.schema.keys())
set(rec['properties'].keys()) == set(c.schema['properties'].keys())
###############################################################################
pprint(fiona.FIELD_TYPES_MAP)
###############################################################################
type(rec['properties']['CNTRY_NAME'])
c.schema['properties']['CNTRY_NAME']
###############################################################################
from fiona import prop_width
prop_width('str:25')
prop_width('str')
###############################################################################
from fiona import prop_type
prop_type('int')
prop_type('float')
prop_type('str:25')
###############################################################################
import fiona
from pprint import pprint
c = fiona.open('/gdata/world_borders.shp')
rec = c.next()
pprint(rec)
###############################################################################
c.close()
rec['id']
###############################################################################
c = fiona.open('/gdata/world_borders.shp')
rec = next(c)
rec['id']
###############################################################################
pprint(rec['properties'])
###############################################################################
pprint(rec['geometry'])
###############################################################################
from shapely.geometry import shape
l1 = shape({'type': 'LineString', 'coordinates': [(0, 0), (2, 2)]})
l2 = shape({'type': 'LineString', 'coordinates': [(0, 0), (1, 1), (2, 2)]})
l1 == l2
l1.equals(l2)
