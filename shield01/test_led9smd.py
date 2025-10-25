# (c) OctopusLAB 2017-25 - MIT
# simple LED_BLINK test

from time import sleep_ms
from machine import Pin

led = Pin(9, Pin.OUT)


while True:
    led.value(1)
    sleep_ms(500)
    led.value(0)
    sleep_ms(500)