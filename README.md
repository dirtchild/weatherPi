# weatherPi
This is Prototype 2. Reworked all code after the [first prototype](https://github.com/dirtchild/rpi_projects/tree/master/weather.piZero). I was going to rework that code but it was ugly, needed an overhaul, I didn't like the structure of it and I didn't want to mess with an existing repo. This is the software behind a personal weather station based around a raspberry pi zero w. It uses a few adafruit sensors along with a four channel ADC and external senors which are sold as spare parts. Its all very specific to my build, but would be a good starting point for reuse for others attempting to build something similar.


The code should be relatively well documented. The main funciton is to:

1. Read all attached sensors
1. Send to weather underground
1. Send to remote database for custom display

The project uses a base object for data storage/passing - SensorData. The physical sensors used in this project are, in no particular order:

* Wind Speed 
* Wind Direction
* Rain
* UV
* Temp/alt/pressure
* temp/hum
* ADC

Various design diagrams are in the DesignDocs directory, they may help someone.
