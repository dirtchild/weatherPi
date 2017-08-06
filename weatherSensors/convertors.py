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
   return mm * 0.039370

def voltToUv(v):
    print "UV"

def voltToDegree(v):
    print "degree"

def dewpointF(tempF, hum):
    c = f_to_c(tempF)
    x = 1 - 0.01 * hum;
    dewpoint = (14.55 + 0.114 * c) * x;
    dewpoint = dewpoint + ((2.5 + 0.007 * c) * x) ** 3;
    dewpoint = dewpoint + (15.9 + 0.117 * c) * x ** 14;
    dewpoint = c - dewpoint;
    return c_to_f(dewpoint)
