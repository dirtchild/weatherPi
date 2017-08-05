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
wSpeed = eventSensor(13,1.492,"wspeed","w_spd","MPH")
time.sleep(4)

#p("access sensorLog")
#wSpeed.sensorLog[0].sensor
#wSpeed.sensorLog[0].value
#wSpeed.sensorLog[0].unit

print "UPTO: doesn't look like anything is being logged....."

p("last 5 seconds")
reading = wSpeed.getReading("test",5)
print reading
p("")
p("")
p("")
p("")
p("")
p("")