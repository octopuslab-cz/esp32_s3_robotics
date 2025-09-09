# simple MicroPython example | ESP32 & TM1637
# (c) OctopusLAB 2017-25 - MIT
# voltmeter / battery voltage measurement - TM1637

from time import sleep
from machine import Pin
from utils.pinout import set_pinout
from components.display4 import TM1637Decimal
from components.analog import Analog

pinout = set_pinout()

print("[--- init ---] analog")
an1 = Analog(pinout.BATMES_PIN) # BATMES_PIN 5
an1.adc_test()
an1.get_adc_aver(20)

def raw_to_volts(raw):
    U0 = 0.0      # voltage at zero
    R0 = 15       # raw value at zero
    U1 = 4.75     # voltage at max
    R1 = 2850     # raw value at max    
    return (raw - R0) * (U1 - U0) / (R1 - R0) + U0

# an1.adc.atten(ADC.ATTN_2_5DB) # Full range: 3.3V

print("[--- init ---] display4")
# tm = TM1637Decimal(clk=Pin(18), dio=Pin(19)) # DoIt
# tm = TM1637Decimal(clk=Pin(47), dio=Pin(9))  # S3
tm = TM1637Decimal(clk=Pin(pinout.P2_PIN), dio=Pin(pinout.P3_PIN))

tm.show("----")

for i in range(7):
    tm.show("--"+str(7-i))
    sleep(0.3)

tm.show('abcd')
sleep(2)

# for i in range(6):
while True:
    v = an1.get_adc_aver(20)
    print(v, raw_to_volts(v))
    tm.show('    ')
    tm.show(str(raw_to_volts(v)))
    sleep(0.5)
