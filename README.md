# weatherPi

## About
This is the software behind the second prototype of a personal weather station based around a raspberry pi zero w. This is a complete restart of the code from the [first prototype](https://github.com/dirtchild/rpi_projects/tree/master/weather.piZero). I was going to reuse that code but it was ugly, needed an overhaul, I didn't like the structure of it and I didn't want to mess with an existing repo. The weather station itself uses a few adafruit sensors along with a four channel ADC attached to external senors (which are sold as weather station spare parts). It has a custom case built around a water bottle and an embedded solar fan to negate heat fluctuations from direct sunlight. Its all very specific to my build, but would be a good starting point for reuse for others attempting to build something similar.

## Purpose
The code should be relatively well documented and easy to follow. The main funciton is to:

1. Read all attached sensors
1. Send the gathered data to
    * weather underground
    * Metoffice WOW service (UK)
    * a remote database (I use this to generate a basic current conditions page).

## Python Module Dependencies

* Adafruit_DHT
* Adafruit_Python_ADS1x15
* MySQLdb
* RPi.GPIO
* smbus
* urllib2
* WeatherSensors (in this repo)

## Hardware
The hardware used in this project, in no particular order:

* [Adafruit MPL3115A2](https://www.adafruit.com/product/1893) Barometric Pressure, Altitude & Temperature
* [ADS1015 ADC Module](https://www.adafruit.com/product/1083) - 12 Bit I2C 4 Channel
* [Generic UV sensor](https://www.amazon.co.uk/dp/B00NL9XNN8/ref=pe_3187911_189395841_TE_3p_dp_1) (analogue. ASIN: B00NL9XNN8)
* [Maplin N96FY Wind Speed](http://www.maplin.co.uk/p/maplin-replacement-wind-speed-sensor-for-n96fy-n82nf)
* [Rainfall](https://www.amazon.co.uk/dp/B00QDMBXUA/ref=pe_3187911_189395841_TE_3p_dp_1) (generic spare part)
* [Raspberry pi Zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/)
* [Solar Powered Clip Fan](https://images-na.ssl-images-amazon.com/images/I/51NwW1oJ6fL._SY355_.jpg) - ripped apart and mounted into the housing cowel
* [some snaps of the housing](http://imgur.com/a/DPmJf) to get an idea of how it's setup
* [Wind Direction](https://www.amazon.co.uk/dp/B00FQGV8RM/ref=pe_3187911_189395841_TE_3p_dp_1) (generic spare part)
* MPL3115A2 Generic temperature & Humidity sensor - from a [bulk lot of sensors](http://www.gearbest.com/kits/pp_447873.html)

## Design
Various design diagrams are in the DesignDocs directory, they may help someone. All sensor data passing is carried out using a custom data structure, SensorData. For consistency (and because data is uploaded to Wunderground), I use the labels set out in the [Weather Underground PWS API](http://wiki.wunderground.com/index.php/PWS_-_Upload_Protocol) when dealing with labeled sensor readings e.g. `baromin` for barometric pressure. The units defined by the wunderground API are also used for consistency if nothing more (even though it feels wrong to be using imperial measurements it's easy enough to convert things to something more sensible on display).

Note that there are two temperature sensors in use here (not by design - the humidity and barometric pressure sensors came with extras). These are mounted in the enclosure with the rPi/rest of the internals. Although there is a fan and all endeavours have been made to equyalise the temperature inside the casing with the outside air (venting, painted white, fan etc), both readings are averaged and then normalised against the CPU temperature to try and get an actual air temperature.
