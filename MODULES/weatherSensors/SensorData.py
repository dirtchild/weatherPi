#!/usr/bin/env python

########################################################################
## This file defines an atomic type for passing weather data
##
## * label (string): the title - for consistency, all labels will follow 
##   those set out in the Wunderground PWS API: http://wiki.wunderground.com/index.php/PWS_-_Upload_Protocol
## * value (int): the reading
## * unit (string): what we are measuring 
## * timeStamp: when it was created/taken. timestamp in seconds since epoch
##
## CREATED:  2017-07-17
## MODIFIED: see https://github.com/dirtchild/weatherPi
##

import time
global sensor
global label
global value
global unit
global timeStamp

class SensorReading:
	def __init__(self, sensor, label, value, unit, timeStamp=None):
		self.sensor = sensor
		self.label = label
		self.value = value
		self.unit = unit
		if timeStamp is None:
			self.timeStamp = time.time()
		else:	
			self.timeStamp = timeStamp

	def __repr__(self):
		return "[SensorReading] self.sensor>>[%s]  self.label>>[%s]  self.value>>[%s]   self.unit>>[%s]  self.timeStamp>>[%s]" % (self.sensor, self.label, self.value, self.unit, self.timeStamp)
