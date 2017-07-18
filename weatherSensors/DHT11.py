#!/usr/bin/env python

# reads data from an adafruit DHT11 temp/humidity sensor
# RETURNS: two objects for humidity and temperature
# CREATED: 2017-07-18
# MODIFIED: see https://github.com/dirtchild/weatherPi

import Adafruit_DHT
import SensorData.SensorReading

class DHT11:
	# pin the dht is connected to
	gpio = 23

	def getData():
		# grab it
		hum, tem = Adafruit_DHT.read_retry(11, self.gpio)
		# create our data returns
		# F: sensor, label, value, unit
		dhtHum = SensorReading("dht11", "humidity", hum, "%")
		dhtTem = SensorReading("dht11", "temperature", tem, "f")
		# return them

		return (dhtTem,dhtHum)