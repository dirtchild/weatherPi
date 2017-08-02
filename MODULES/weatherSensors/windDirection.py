#!/usr/bin/env python

# reads data from wind direction thingy (see README)
# labels follow those set out in the Wunderground PWS API: 
#	http://wiki.wunderground.com/index.php/PWS_-_Upload_Protocol
#
# SOURCES:
# RETURNS: two objects for humidity and temperature
# CREATED: 2017-08-02
# MODIFIED: see https://github.com/dirtchild/weatherPi

import SensorData.SensorReading

def getReading():