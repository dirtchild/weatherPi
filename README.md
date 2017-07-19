# weatherPi
This is the software behind the second prototype of a personal weather station based around a raspberry pi zero w. This is a complete restart of the code from the [first prototype](https://github.com/dirtchild/rpi_projects/tree/master/weather.piZero). I was going to reuse that code but it was ugly, needed an overhaul, I didn't like the structure of it and I didn't want to mess with an existing repo. The weather station itself uses a few adafruit sensors along with a four channel ADC attached to external senors (which are sold as weather station spare parts). It has a custom case built around a water bottle (yes, really really a water bottle, with venting) and an embedded solar fan to negate heat fluctuations from direct sunlight. Its all very specific to my build, but would be a good starting point for reuse for others attempting to build something similar.


The code should be relatively well documented and easy to follow. The main funciton is to:

1. Read all attached sensors
1. Send the gathered data to
    * weather underground 
    * a remote database (I use this to generate a basic current conditions page). 

The hardware used in this project, in no particular order:

* [Wind Speed](https://www.amazon.co.uk/dp/B00FQGV78C/ref=pe_3187911_189395841_TE_3p_dp_2) (generic spare part)
* [Wind Direction](https://www.amazon.co.uk/dp/B00FQGV8RM/ref=pe_3187911_189395841_TE_3p_dp_1) (generic spare part)
* [Rainfall](https://www.amazon.co.uk/dp/B00QDMBXUA/ref=pe_3187911_189395841_TE_3p_dp_1) (generic spare part)
* [Generic UV sensor](https://www.amazon.co.uk/dp/B00NL9XNN8/ref=pe_3187911_189395841_TE_3p_dp_1) (analogue. ASIN: B00NL9XNN8)
* [Adafruit MPL3115A2](https://www.adafruit.com/product/1893) Barometric Pressure, Altitude & Temperature
* MPL3115A2 Generic temperature & Humidity sensor - from a [bulk lot of sensors](http://www.gearbest.com/kits/pp_447873.html)
* [ADS1015 ADC Module](https://www.adafruit.com/product/1083) - 12 Bit I2C 4 Channel
* [Raspberry pi Zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/)
* [Solar Powered Clip Fan](https://images-na.ssl-images-amazon.com/images/I/51NwW1oJ6fL._SY355_.jpg) - ripped apart and mounted into the housing cowel
* [some snaps of the housing](http://imgur.com/a/hO6tJ) to get an idea of how it's setup

Note that there are two temperature sensors in use here. These are enclosed with the PCB/rest of the internals. Although there is a fan and all endeavours have been made to normalise the temperature inside the casing (venting, painted white, fan etc), both readings are averaged and then normalised against the CPU temperature to try and get an actual air temperature. Various design diagrams are in the DesignDocs directory, they may help someone.

All sensor data passing is carried out using a custom data structure, SensorData. For consistency (and because it's existing and well defined), we use the labels set out in the [Weather Underground PWS API](http://wiki.wunderground.com/index.php/PWS_-_Upload_Protocol) when dealing with labeled sensor readings e.g. `baromin` for barometric pressure. We also use the units defined there for consistency where possible (even though it feels wrong to be using imperial measurements).
