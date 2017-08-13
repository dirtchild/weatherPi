import sys
from convertors import *
degree = voltToDeg(sys.argv[1],3.3,0)
print(degree)
print windDirectionFromDegrees(degree)
