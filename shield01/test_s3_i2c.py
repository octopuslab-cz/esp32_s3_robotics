# (c) OctopusLAB 2017-25 - MIT

from machine import Pin, I2C
from utils.pinout import set_pinout
    
pinout = set_pinout()
# i = I2C(scl=Pin(22), sda=Pin(21), freq=f)
# HW or SW: HW 0 - | SW -1
i2c = I2C(scl=Pin(pinout.I2C_SCL_PIN), sda=Pin(pinout.I2C_SDA_PIN))
    
print(i2c.scan())