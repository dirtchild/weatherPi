# ORIGINAL SOURCE: https://github.com/dirtchild/weatherPi [please do not remove this line]

import sys
from convertors import *
degree = voltToDeg(sys.argv[1],3.3,0)
print(degree)
print windDirectionFromDegrees(degree)
