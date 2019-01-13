#!/usr/bin/env python

# read data from an event driven sensor. Generalised for use with any event-based sensor
#
# SOURCES:
#		* http://wiki.wunderground.com/index.php/PWS_-_Upload_Protocol
# RETURNS: SensorData.SensorReading object
# CREATED: 2017-08-02
# ORIGINAL SOURCE: https://github.com/dirtchild/weatherPi [please do not remove this line]
# MODIFIED: see https://github.com/dirtchild/weatherPi

import RPi.GPIO as GPIO
from SensorData import SensorReading
import time

class eventSensor:

	# * gpioToread: data pin, in GPIO notation
	# * calibration: what one even means. e.g. how many mm in one rain bucket tip
	# * sensor: the name of the sensor
	# * label: the wunderground PWS label
	# * unit: what it's being measured in
	def __init__(self, gpioToRead, calibration, sensor, label, unit, periodToKeep):
		self.gpioToRead = gpioToRead
		self.calibration = calibration
		self.sensor = sensor
		self.label = label
		self.unit = unit
		self.sensorLog = []
		self.periodToKeep = periodToKeep

		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.gpioToRead, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(self.gpioToRead, GPIO.FALLING, callback=self.logSensorEvent, bouncetime=300)

	def __exit__(self, exc_type, exc_value, traceback):
		GPIO.cleanup()

	def __repr__(self):
		return "[eventSensor]\n\tself.gpioToRead [",self.gpioToRead,"]\n\t self.calibration [",self.calibration,"]\n\t self.sensor [",self.sensor,"]\n\t self.label [",self.label,"]\n\t self.unit [",self.unit,"]"

	# the call back function for each bucket tip
	def logSensorEvent(self,channel):
		global sensorLog
		# add to the global sensor array
		self.sensorLog.append(SensorReading(self.sensor,self.label,self.calibration,self.unit))
		# remove last until no more older than periodToKeep
		while (time.time() - self.sensorLog[0].timeStamp) >= self.periodToKeep:
			del self.sensorLog[0]

	# label: as per wunderground
	# period: in seconds. how far back you want to go
	def getPeriodTotal(self,newLabel, period):
		global sensorLog
		thisSum=0
		# need to have some readings for this to make sense
		if len(self.sensorLog) > 0:
			for thisReading in self.sensorLog:
				if (time.time() - thisReading.timeStamp) <= period:
					thisSum += thisReading.value
		return(SensorReading(self.sensor,newLabel,thisSum,self.unit))

	# label: as per wunderground
	# period: in seconds. how far back you want to go
	def getPeriodAverage(self,newLabel, period):
		global sensorLog
		thisSum=0
		cnt=0
		# need to have some readings for this to make sense
		if len(self.sensorLog) > 0:
			for thisReading in self.sensorLog:
				if (time.time() - thisReading.timeStamp) <= period:
					thisSum += thisReading.value
		return(SensorReading(self.sensor,newLabel,thisSum/period,self.unit))

	# label: as per wunderground
	# period: in seconds. how far back you want to go
	def getLast(self):
		global sensorLog
		if len(self.sensorLog) > 0:
			return(self.sensorLog[-1])
		else:
			return(SensorReading(self.sensor,self.label,0,self.unit))
