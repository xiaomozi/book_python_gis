#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import geopandas as gpd
import matplotlib.pyplot as plt
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world = world[(world.pop_est>0) & (world.name!="Antarctica")]
world['gdp_per_cap'] = world.gdp_md_est / world.pop_est
world.plot(column='gdp_per_cap');
plt.show()
###############################################################################
world.plot(column='gdp_per_cap', cmap='OrRd');
plt.show()
###############################################################################
world.plot(column='gdp_per_cap', cmap='OrRd', scheme='quantiles');
plt.show()
###############################################################################
cities = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))
cities.plot(marker='*', color='green', markersize=5);
# Check crs
cities = cities.to_crs(world.crs)
# Now we can overlay over country outlines
# And yes, there are lots of island capitals
# apparently in the middle of the ocean!
###############################################################################
base = world.plot(color='white')
cities.plot(ax=base, marker='o', color='red', markersize=5);
plt.show()
