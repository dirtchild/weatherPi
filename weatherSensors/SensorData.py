#!/usr/bin/env python

########################################################################
## This file defines an atomic type for passing weather data
##
## * label (string): the title - UID for this measurement
## * value (int): the reading
## * unit (string): what we are measuring 
##
## CREATED: 
## MODIFIED: see https://github.com/dirtchild/weatherPi
##

class SensorData:
    def __init__(self, label, value, unit):
	    self.label = label
		self.value = value
		self.unit = unit