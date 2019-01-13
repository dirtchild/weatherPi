#!/usr/bin/env python

# reads data from wind direction thingy (see README)
# labels follow those set out in the Wunderground PWS API:
#	http://wiki.wunderground.com/index.php/PWS_-_Upload_Protocol
#
# SOURCES:
#   * https://learn.sparkfun.com/tutorials/ml8511-uv-sensor-hookup-guide
#   * https://github.com/nickoala/sensor/blob/master/sensor/ML8511.py
#   * Adafruit_ADS1x15 library examples
# RETURNS: two objects for humidity and temperature
# CREATED: 2017-08-02
# ORIGINAL SOURCE: https://github.com/dirtchild/weatherPi [please do not remove this line]
# MODIFIED: see https://github.com/dirtchild/weatherPi

from SensorData import SensorReading
from convertors import *
import time
import Adafruit_ADS1x15

def getReading():
	# Choose a gain of 1 for reading voltages from 0 to 4.09V.
	# Or pick a different gain to change the range of voltages that are read:
	#  - 2/3 = +/-6.144V
	#  -   1 = +/-4.096V
	#  -   2 = +/-2.048V
	#  -   4 = +/-1.024V
	#  -   8 = +/-0.512V
	#  -  16 = +/-0.256V
	# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
	# see UV csensor data sheet: https://cdn.sparkfun.com/datasheets/Sensors/LightImaging/ML8511_3-8-13.pdf
	GAIN = 2/3

	# the channel on the ADC to use
	CHANNEL = 1

	# Create an ADS1115 ADC (16-bit) instance and do stuff with it
	adc = Adafruit_ADS1x15.ADS1115()
	adc.start_adc(CHANNEL, gain=GAIN)
	start = time.time()
	value = 0
	cnt = 0
	totalVoltage = 0
	while (time.time() - start) <= 5.0:
	    totalVoltage += adc.get_last_result()
	    cnt += 1
	    time.sleep(0.5)
	# Stop continuous conversion.  After this point you can't get data from get_last_result!
	adc.stop_adc()
	avgVoltage = totalVoltage / cnt
	return(SensorReading("uv", "UV", voltToUvIndex(avgVoltage), "index [DEBUG: bad math]"),SensorReading("solarradiation", "solarradiation", avgVoltage, "W/m^2"))
