#!/usr/bin/env python
########################################################################
#
#			Jiwan Ninglekhu
#			11/30/2015
#			mapper function 
#
########################################################################


import sys
from datetime import date
import datetime
import calendar

for line in sys.stdin:
    line = line.strip()
    unpacked = line.split(",")
    stadium, capacity, expanded, location, surface, turf, team, opened, weather, roof, elevation = line.split(",")
 

    print '%s\t%s' % (turf, 1)
  
