# various things to convert between things
# CREATED: 2017-07-18
# https://github.com/dirtchild/weatherPi

# celcius to farenheight
def c_to_f(input_temp):
    return (input_temp * 1.8) + 32

def kpaToInches(kpa):
   return kpa * 0.295301

def mmToInches(mm):
   return mm * 0.039370
