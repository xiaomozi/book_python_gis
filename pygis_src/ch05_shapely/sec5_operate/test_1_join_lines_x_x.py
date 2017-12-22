#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
from shapely.ops import polygonize
lines = [
    ((0, 0), (1, 1)),
    ((0, 0), (0, 1)),
    ((0, 1), (1, 1)),
    ((1, 1), (1, 0)),
    ((1, 0), (0, 0))
    ]
###############################################################################
from shapely.ops import linemerge
linemerge(lines)
print(list(linemerge(lines)))
