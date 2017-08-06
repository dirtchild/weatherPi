#!/usr/bin/env python

# reads data from wind direction thingy (see README)
# labels follow those set out in the Wunderground PWS API: 
#	http://wiki.wunderground.com/index.php/PWS_-_Upload_Protocol
#
# SOURCES:
# RETURNS: two objects for humidity and temperature
# CREATED: 2017-08-02
# MODIFIED: see https://github.com/dirtchild/weatherPi

from SensorData import SensorReading 
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
	GAIN = 1

	# the channel on the ADC to use
	CHANNEL = 0

	# scaling and transposing voltage reading to actual direction
	# based on 5v supply, 100k resistor (needs scaling) - see: https://www.argentdata.com/files/80422_datasheet.pdf
	# will be (degree|voltage)
	voltToDegree = {}

	voltToDegree["3.84"] = 0.0
	voltToDegree["1.98"] = 22.5
	voltToDegree["2.25"] = 45.0
	voltToDegree["0.41"] = 67.5
	voltToDegree["0.45"] = 90.0
	voltToDegree["0.32"] = 112.5
	voltToDegree["0.90"] = 135.0
	voltToDegree["0.62"] = 157.5
	voltToDegree["1.40"] = 180.0
	voltToDegree["1.19"] = 202.5
	voltToDegree["3.08"] = 225.0
	voltToDegree["2.93"] = 247.5
	voltToDegree["4.62"] = 270.0
	voltToDegree["4.04"] = 292.5
	voltToDegree["4.78"] = 315.0
	voltToDegree["3.43"] = 337.5

	# Create an ADS1115 ADC (16-bit) instance and do stuff with it
	adc = Adafruit_ADS1x15.ADS1115()
	adc.start_adc(CHANNEL, gain=GAIN)
	start = time.time()
	value = 0
	totalVoltage = 0
	cnt = 0
	while (time.time() - start) <= 5.0:
	    totalVoltage += adc.get_last_result()
	    cnt += 1
	    time.sleep(0.5)
	# Stop continuous conversion.  After this point you can't get data from get_last_result!
	adc.stop_adc()
	avgVoltage = totalVoltage / cnt

	# DEBUG: should be voltToDegree["avgVoltage"]
	return(SensorReading("winddir", "winddir", avgVoltage, "degree angle [DEBUG: avgVoltage]"))

