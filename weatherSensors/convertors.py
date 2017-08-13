# various things to convert between things
# CREATED: 2017-07-18
# https://github.com/dirtchild/weatherPi
# a lot of this is taken from the following, and modified to suit:
#	https://sourceforge.net/projects/meta-tools/files/pyweather/0.7.0/

import math

# celcius to farenheight
def c_to_f(input_temp):
    return (input_temp * 1.8) + 32

def f_to_c(input_temp):
    return (input_temp - 32) / 1.8

def kpaToInches(kpa):
   return kpa * 0.295301

def mmToInches(mm):
    return float(mm) * 0.039370

def voltToUvIndex(v):
    # DEBUG. taken from: https://docs.bsfrance.fr/documentation/10454_GYML8511/MP8511_Read_Example.ino
    # no idea how it works, but it's used ina  few places, so copy and paste!
    in_min = 0.99
    in_max = 2.9
    out_min = 0.0
    out_max = 15.0
    # seemed like it was off by 1k. so I twiddled
    return (round(((v - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)/1000,2))

def dewpointF(tempF, hum):
    c = f_to_c(tempF)
    x = 1 - 0.01 * hum;
    dewpoint = (14.55 + 0.114 * c) * x;
    dewpoint = dewpoint + ((2.5 + 0.007 * c) * x) ** 3;
    dewpoint = dewpoint + (15.9 + 0.117 * c) * x ** 14;
    dewpoint = c - dewpoint;
    return c_to_f(dewpoint)

#####################################################
# everything from here down is borrowed from:
#   https://github.com/kmkingsbury/raspberrypi-weather-station/issues/8#issuecomment-169661343
#
def voltToDeg(vRead,vPower,dirAdjust):
    global lastwinddir
    #DEBUG: need to get this value from way up in the main main()
    #DEBUG: fudged when testing because effort
    lastwinddir = 0
    winddir_voltage = ConvertVoltage (float(vRead), vPower)
    winddir = voltageToDegrees(winddir_voltage, lastwinddir)
    #Mounted windvane improperly (not facing north) so adjusting in the software
    winddir = AdjustWindDir(winddir, dirAdjust)
    lastwinddir = winddir
    #DEBUG, needed?: capitalwinddir = windDirectionFromDegrees(winddir)
    return(winddir)


# convert light into percent
def ConvertVoltage(data, supplyVolt):
  voltage = data/1024. * supplyVolt #// convert to voltage value
  return voltage

def ConvertPercent (data, supplyVolt, places):
  percent = (data / supplyVolt) * 100
  percent = round(percent,places)
  return percent

def fuzzyCompare(compareValue, value):
    VARYVALUE = 0.05
    if ( (value > (compareValue * (1.0-VARYVALUE)))  and (value < (compareValue *(1.0+VARYVALUE))) ):
        return True
    return False

def voltageToDegrees(value, defaultWindDirection):
    ADJUST3OR5 = 0.66
    PowerVoltage = 3.3
    if (fuzzyCompare(3.84 * ADJUST3OR5, value)):
        return 0.0
    if (fuzzyCompare(1.98 * ADJUST3OR5, value)):
        return 22.5
    if (fuzzyCompare(2.25 * ADJUST3OR5, value)):
        return 45
    if (fuzzyCompare(0.41 * ADJUST3OR5, value)):
        return 67.5
    if (fuzzyCompare(0.45 * ADJUST3OR5, value)):
        return 90.0
    if (fuzzyCompare(0.32 * ADJUST3OR5, value)):
        return 112.5
    if (fuzzyCompare(0.90 * ADJUST3OR5, value)):
        return 135.0
    if (fuzzyCompare(0.62 * ADJUST3OR5, value)):
        return 157.5
    if (fuzzyCompare(1.40 * ADJUST3OR5, value)):
        return 180
    if (fuzzyCompare(1.19 * ADJUST3OR5, value)):
        return 202.5
    if (fuzzyCompare(3.08 * ADJUST3OR5, value)):
        return 225
    if (fuzzyCompare(2.93 * ADJUST3OR5, value)):
        return 247.5
    if (fuzzyCompare(4.62 * ADJUST3OR5, value)):
        return 270.0
    if (fuzzyCompare(4.04 * ADJUST3OR5, value)):
        return 292.5
    if (fuzzyCompare(4.34 * ADJUST3OR5, value)): # chart in manufacturers documentation wrong
        return 315.0
    if (fuzzyCompare(3.43 * ADJUST3OR5, value)):
        return 337.5
    return defaultWindDirection  # return previous value if not found

def windDirectionFromDegrees (Degrees):
    if (348.75 <= Degrees <= 360.00):
        hour1WindDirection = "N"
    elif (0 <= Degrees <= 11.25):
        hour1WindDirection = "N"
    elif (11.25 < Degrees <= 33.75):
        hour1WindDirection = "NNE"
    elif (33.75 < Degrees <= 56.25):
        hour1WindDirection = "NE"
    elif (56.25 < Degrees <= 78.75):
        hour1WindDirection = "ENE"
    elif (78.75 < Degrees <= 101.25):
        hour1WindDirection = "E"
    elif (101.25 < Degrees <= 123.75):
        hour1WindDirection = "ESE"
    elif (123.75 < Degrees <= 146.25):
        hour1WindDirection = "SE"
    elif (146.25 < Degrees <= 168.75):
        hour1WindDirection = "SSE"
    elif (168.75 < Degrees <= 191.25):
        hour1WindDirection = "S"
    elif (191.25 < Degrees <= 213.75):
        hour1WindDirection = "SSW"
    elif (213.75 < Degrees <= 236.25):
        hour1WindDirection = "SW"
    elif (236.25 < Degrees <= 258.75):
        hour1WindDirection = "WSW"
    elif (258.75 < Degrees <= 281.25):
        hour1WindDirection = "W"
    elif (281.25 < Degrees <= 303.75):
        hour1WindDirection = "WNW"
    elif (303.75 < Degrees <= 326.25):
        hour1WindDirection = "NW"
    elif (326.25 < Degrees < 348.75):
        hour1WindDirection = "NNW"
    else:
        hour1WindDirection = nil
    return hour1WindDirection

def AdjustWindDir(data,adjustor):
  #if current wind direction in degrees is less than 90
  if (data < adjustor):
    #add 360 before subtracting 90
    adjustedwinddir = (data + 360.00) - adjustor
  #otherwise, simply subtract 90
  else:
    adjustedwinddir = (data - adjustor)
  #return the compensated value
  return adjustedwinddir
