## taken from: https://github.com/ControlEverythingCommunity/MPL3115A2/blob/master/Python/MPL3115A2.py
# github@dirtchild.net
# created: 2017-05-14




# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# MPL3115A2
# This code is designed to work with the MPL3115A2_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/products

import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

# MPL3115A2 address, 0x60(96)
# 0x48 = ? 
data = bus.read_i2c_block_data(0x48, 0x00, 6)

# Output data to screen
print data 
