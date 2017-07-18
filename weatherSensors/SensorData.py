#!/usr/bin/env python

########################################################################
## This file defines an atomic type for passing weather data
##
## * label (string): the title - UID for this measurement
## * value (int): the reading
## * unit (string): what we are measuring 
## * timestamp: when it was created/taken
##
## CREATED: 
## MODIFIED: see https://github.com/dirtchild/weatherPi
##

import time

class SensorReading:
	def __init__(self, sensor, label, value, unit, timestamp=None):
		self.sensor = sensor
		self.label = label
		self.value = value
		self.unit = unit
		if timestamp is None:
			self.timestamp = time.time()
		else:	
			self.timestamp = timestamp