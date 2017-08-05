#! /usr/bin/python

# this is a very basic (read not big enough for testdoc or unit test or anything more formal) to test
# the event based sensor readings.

def p(message):
	print "[",message,"]"

p("import")	
from eventSensor import eventSensor
import time
import sys

p("class instantiate")
# * gpioToread: data pin, in GPIO notation
# * calibration: what one even means. e.g. how many mm in one rain bucket tip
# * sensor: the name of the sensor
# * label: the wunderground PWS label
# * unit: what it's being measured in
# * periodToKeep: in seconds. how many log entries to keep. will kill memory if it's too big
#	86400 seconds = 1 day
#	3600 seconds = 1 hour

wSpeed = eventSensor(13,1.492,"wspeed event","w_spd","MPH",90000)
rain = eventSensor(6,0.2794,"rain event","rain","mm",90000)

p("do some readings")
while True:
	time.sleep(5)
	print wSpeed.getPeriodTotal("WS 1M",60)               
	print wSpeed.getPeriodTotal("WS 1H",3600)               
	#print wSpeed.getPeriodTotal("WS 1D",86400)
	print rain.getPeriodTotal("RAIN 1M",60)
	print rain.getPeriodTotal("RAIN 1H",3600)
	#print rain.getPeriodTotal("RAIN 1D",86400)
	print "-------------------------------------------------------------------------------"
	sys.stdout.flush()
