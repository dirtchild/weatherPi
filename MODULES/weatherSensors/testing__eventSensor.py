#! /usr/bin/python

# this is a very basic (read not big enough for testdoc or unit test or anything more formal) to test
# the event based sensor readings.

def p(message):
	print "[",message,"]"

p("import")	
from eventSensor import eventSensor
import time

p("class instantiate")
# * gpioToread: data pin, in GPIO notation
# * calibration: what one even means. e.g. how many mm in one rain bucket tip
# * sensor: the name of the sensor
# * label: the wunderground PWS label
# * unit: what it's being measured in
wSpeed = eventSensor(13,1.492,"wspeed event","w_spd","MPH")
#rain = eventSensor(6,0.2794,"rain event","rain","mm")

while True:
	time.sleep(5)
	#DEBUG
	print "UPTO: not giving an average!!! rain is totally wrong, but multiples of the correct thing.... logic is wrong. we have a line of ticks... adding then dividing by the number is wrong. should be sum and divide by time!!!! e.g rain is mm per minute etc.... check the /testing/rain.py"
		
	print wSpeed.getAvgReading("WS 10sec",10)
	#print rain.getSumReading("rain10sec",10)
	

#p("")
#p("")
#p("")
