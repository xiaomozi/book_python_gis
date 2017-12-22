#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
###############################################################################
from matplotlib import pyplot as plt
from shapely.geometry import LineString
from descartes import PolygonPatch
BLUE = '#6699cc'
GRAY = '#999999'
###############################################################################
def plot_line(ax, ob):
    x, y = ob.xy
    ax.plot(x, y, color=GRAY, linewidth=3, solid_capstyle='round', zorder=1)
###############################################################################
line = LineString([(0, 0), (1, 1), (0, 2), (2, 2), (3, 1), (1, 0)])
fig = plt.figure(1, figsize=(10, 4), dpi=180)
###############################################################################
ax = fig.add_subplot(121)
###############################################################################
# plot_l 5555555ine(ax, line)
dilated = line.buffer(0.5)
patch1 = PolygonPatch(dilated, fc=BLUE, ec=BLUE, alpha=0.5, zorder=2)
ax.add_patch(patch1)
#2
ax = fig.add_subplot(122)
patch2a = PolygonPatch(dilated, fc=GRAY, ec=GRAY, alpha=0.5, zorder=1)
ax.add_patch(patch2a)
eroded = dilated.buffer(-0.3)
###############################################################################
# GeoJSON-like data works as well
polygon = eroded.__geo_interface__
# >>> geo['type']
# 'Polygon'
# >>> geo['coordinates'][0][:2]
# ((0.50502525316941682, 0.78786796564403572), (0.5247963548222736, 0.8096820147509064))
patch2b = PolygonPatch(polygon, fc=BLUE, ec=BLUE, alpha=0.5, zorder=2)
ax.add_patch(patch2b)
plt.show()
###############################################################################
from matplotlib import pyplot as plt
from shapely.geometry import *
from descartes import PolygonPatch
fig = plt.figure(num=1, figsize=(10, 4), dpi=180)
###############################################################################
polygon = Point(0, 0).buffer(10.0).difference(
    MultiPoint([(-5, 0), (5, 0)]).buffer(3.0))
polygon
###############################################################################
# 1
ax = fig.add_subplot(221)
###############################################################################
patch = PolygonPatch(polygon, facecolor='#cccccc', edgecolor='#999999')
ax.add_patch(patch)
###############################################################################
minx, miny, maxx, maxy = polygon.bounds
w, h = maxx - minx, maxy - miny
ax.set_xlim(minx - 0.2*w, maxx + 0.2*w)
ax.set_ylim(miny - 0.2*h, maxy + 0.2*h)
ax.set_aspect(1)
###############################################################################
# 2
ax = fig.add_subplot(222)
###############################################################################
geo = polygon.__geo_interface__
patch = PolygonPatch(geo, facecolor='#cccccc', edgecolor='#999999')
ax.add_patch(patch)
###############################################################################
minx, miny, maxx, maxy = polygon.bounds
w, h = maxx - minx, maxy - miny
ax.set_xlim(minx - 0.2*w, maxx + 0.2*w)
ax.set_ylim(miny - 0.2*h, maxy + 0.2*h)
ax.set_aspect(1)
###############################################################################
multipolygon = Point(0, 0).buffer(10.0).difference(
    MultiPoint([(-5, 0), (5, 0)]).buffer(3.0)).union(
    MultiPoint([(-10, 10), (10, -10)]).buffer(2.0))
###############################################################################
# 3
ax = fig.add_subplot(223)
###############################################################################
patch = PolygonPatch(multipolygon, facecolor='#cccccc', edgecolor='#999999')
ax.add_patch(patch)
###############################################################################
minx, miny, maxx, maxy = polygon.bounds
w, h = maxx - minx, maxy - miny
ax.set_xlim(minx - 0.2*w, maxx + 0.2*w)
ax.set_ylim(miny - 0.2*h, maxy + 0.2*h)
ax.set_aspect(1)
###############################################################################
# 4
# Create a subplot
ax = fig.add_subplot(224)
###############################################################################
geo = multipolygon.__geo_interface__
patch = PolygonPatch(geo, facecolor='#cccccc', edgecolor='#999999')
ax.add_patch(patch)
###############################################################################
minx, miny, maxx, maxy = polygon.bounds
w, h = maxx - minx, maxy - miny
ax.set_xlim(minx - 0.2*w, maxx + 0.2*w)
ax.set_ylim(miny - 0.2*h, maxy + 0.2*h)
ax.set_aspect(1)
plt.show()
###############################################################################
from matplotlib import pyplot as plt
from shapely.geometry import LineString
from descartes import PolygonPatch
BLUE = '#6699cc'
GRAY = '#999999'
def plot_line(ax, ob):
    x, y = ob.xy
    ax.plot(x, y, color=GRAY, linewidth=3, solid_capstyle='round', zorder=1)
line = LineString([(0, 0), (1, 1), (0, 2), (2, 2), (3, 1), (1, 0)])
fig = plt.figure(1, figsize=(10, 4), dpi=180)
# 1
ax = fig.add_subplot(121)
plot_line(ax, line)
dilated = line.buffer(0.5)
patch1 = PolygonPatch(dilated, fc=BLUE, ec=BLUE, alpha=0.5, zorder=2)
ax.add_patch(patch1)
#2
ax = fig.add_subplot(122)
patch2a = PolygonPatch(dilated, fc=GRAY, ec=GRAY, alpha=0.5, zorder=1)
ax.add_patch(patch2a)
eroded = dilated.buffer(-0.3)
# GeoJSON-like data works as well
polygon = eroded.__geo_interface__
# >>> geo['type']
# 'Polygon'
# >>> geo['coordinates'][0][:2]
# ((0.50502525316941682, 0.78786796564403572), (0.5247963548222736, 0.8096820147509064))
patch2b = PolygonPatch(polygon, fc=BLUE, ec=BLUE, alpha=0.5, zorder=2)
ax.add_patch(patch2b)
plt.show()
