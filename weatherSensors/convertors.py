# various things to convert between things
# CREATED: 2017-07-18
# https://github.com/dirtchild/weatherPi
# a lot of this is taken from the following, and modified to suit:
#	https://sourceforge.net/projects/meta-tools/files/pyweather/0.7.0/

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
    # DEBUG - taken from one of the links in weatherSensors.uv - it's not giving the correct output
    # that's either because:
    #   * UV read gain is wrong
    #   * this is wrong
    return ((v - 1) * 25 / 3.0)

def voltToDegree(v):
    print ("degree)")

def dewpointF(tempF, hum):
    c = f_to_c(tempF)
    x = 1 - 0.01 * hum;
    dewpoint = (14.55 + 0.114 * c) * x;
    dewpoint = dewpoint + ((2.5 + 0.007 * c) * x) ** 3;
    dewpoint = dewpoint + (15.9 + 0.117 * c) * x ** 14;
    dewpoint = c - dewpoint;
    return c_to_f(dewpoint)

def voltToDeg(v):
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
    return (voltToDegree["v"])