#!/usr/bin/env python

# read data from an event driven sensor. Generalised for use with any event-based sensor
#
# SOURCES: 
#		* http://wiki.wunderground.com/index.php/PWS_-_Upload_Protocol
# RETURNS: SensorData.SensorReading object
# CREATED: 2017-08-02
# MODIFIED: see https://github.com/dirtchild/weatherPi

import RPi.GPIO as GPIO
import SensorData.SensorReading as SensorReading
import time

class eventSensor:
	# * gpioToread: data pin, in GPIO notation
	# * calibration: what one even means. e.g. how many mm in one rain bucket tip
	# * sensor: the name of the sensor
	# * label: the wunderground PWS label
	# * unit: what it's being measured in
	def __init__(self, gpioToRead, calibration, sensor, label, unit):
		self.gpioToRead = gpioToRead
		self.calibration = calibration
		self.sensor = sensor
		self.label = label
		self.unit = unit

		GPIO.setmode(GPIO.BCM)  
		GPIO.setup(gpioToRead, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(PIN, GPIO.FALLING, callback=logSensorEvent, bouncetime=300)

	def __exit__(self, exc_type, exc_value, traceback):
		GPIO.cleanup()

	# the call back function for each bucket tip
	def logSensorEvent(channel):
		global sensorLog
		# add to the global sensor array
		sensorLog.append(SensorReading(sensor,label,calibration,unit))
		# remove last until no more older than 24 hours (86400 seconds)
		while (time.time() - sensorLog[0].timeStamp) >= 86400:
			del sensorLog[0]

	# label: as per wunderground
	# period: in seconds. how far back you want to go
	def getAverage(label, period):
		thisSum=0
		thisCnt=0
		for thisReading in sensorLog:
			if (time.time() - thisReading.timeStamp) >= period: 
				thisSum += thisReading.value
				thisCnt += 1
		thisAvg=thisSum/thisCnt
		return(SensorReading(sensor,label,thisAvg,unit))

