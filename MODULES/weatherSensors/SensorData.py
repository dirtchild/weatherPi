#!/usr/bin/env python

########################################################################
## This file defines an atomic type for passing weather data
##
## * label (string): the title - for consistency, all labels will follow 
##   those set out in the Wunderground PWS API: http://wiki.wunderground.com/index.php/PWS_-_Upload_Protocol
## * value (int): the reading
## * unit (string): what we are measuring 
## * timestamp: when it was created/taken
##
## CREATED:  2017-07-17
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