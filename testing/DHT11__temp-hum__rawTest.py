#!/usr/bin/python

# 2017-05-18 github@dirtchild.net
# source: http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/
# reference: https://github.com/adafruit/Adafruit_Python_DHT/blob/master/examples/AdafruitDHT.py

import sys
import Adafruit_DHT

while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 23)
    print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
