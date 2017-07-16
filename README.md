# weatherPi
This is the software behind the second prototype of a personal weather station based around a raspberry pi zero w. This is a complete restart of the code from the [first prototype](https://github.com/dirtchild/rpi_projects/tree/master/weather.piZero). I was going to reuse that code but it was ugly, needed an overhaul, I didn't like the structure of it and I didn't want to mess with an existing repo. The weather station itself uses a few adafruit sensors along with a four channel ADC attached to external senors (which are sold as weather station spare parts). It has a custom case built around a water bottle (yes, really really a water bottle, with venting) and an embedded solar fan to negate heat fluctuations from direct sunlight. Its all very specific to my build, but would be a good starting point for reuse for others attempting to build something similar.


The code should be relatively well documented and easy to follow. The main funciton is to:

1. Read all attached sensors
1. Send the gathered data t
  1. weather underground
  1. a remote database (I use this to generate a basic current conditions page).

The project uses a base object for data storage/passing - SensorData. The physical sensors used in this project are, in no particular order:

* Wind Speed 
* Wind Direction
* Rain
* UV
* Temp/alt/pressure
* temp/hum
* ADC

Various design diagrams are in the DesignDocs directory, they may help someone.
