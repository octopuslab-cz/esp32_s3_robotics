# (c) OctopusLAB 2016-25 - MIT
# led blink OctopusLAB framework

from time import sleep_ms
from utils.pinout import set_pinout
from components.led import Led


print("[--- init ---] pinout / LED")
pinout = set_pinout()
led = Led(pinout.LED1_PIN) # 14

print("[--- test ---] blink 3x")
for blink in range(3):
    led.value(1)
    sleep_ms(500)
    led.value(0)
    sleep_ms(500)