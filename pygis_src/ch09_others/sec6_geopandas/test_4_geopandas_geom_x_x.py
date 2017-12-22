#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import geopandas as gpd
from shapely.geometry import Polygon
polys1 = gpd.GeoSeries([Polygon([(0,0), (2,0), (2,2), (0,2)]),
                       Polygon([(2,2), (4,2), (4,4), (2,4)])])
polys2 = gpd.GeoSeries([Polygon([(1,1), (3,1), (3,3), (1,3)]),
                         Polygon([(3,3), (5,3), (5,5), (3,5)])])
df1 = gpd.GeoDataFrame({'geometry': polys1, 'df1':[1,2]})
df2 = gpd.GeoDataFrame({'geometry': polys2, 'df2':[1,2]})
###############################################################################
ax = df1.plot(color='red')
df2.plot(ax=ax, color='green')
import matplotlib.pyplot as plt
plt.show()
###############################################################################
res_union = gpd.overlay(df1, df2, how='union')
res_union
###############################################################################
ax = res_union.plot()
df1.plot(ax=ax, facecolor='none');
df2.plot(ax=ax, facecolor='none');
plt.show()
###############################################################################
res_intersection = gpd.overlay(df1, df2, how='intersection')
ax = res_intersection.plot()
df1.plot(ax=ax, facecolor='none')
df2.plot(ax=ax, facecolor='none')
plt.show()
###############################################################################
res_symdiff = gpd.overlay(df1, df2, how='symmetric_difference')
ax = res_symdiff.plot()
df1.plot(ax=ax, facecolor='none')
df2.plot(ax=ax, facecolor='none')
plt.show()
###############################################################################
res_difference = gpd.overlay(df1, df2, how='difference')
ax = res_difference.plot()
df1.plot(ax=ax, facecolor='none')
df2.plot(ax=ax, facecolor='none')
plt.show()
###############################################################################
res_identity = gpd.overlay(df1, df2, how='identity')
ax = res_identity.plot()
df1.plot(ax=ax, facecolor='none')
df2.plot(ax=ax, facecolor='none')
plt.show()
