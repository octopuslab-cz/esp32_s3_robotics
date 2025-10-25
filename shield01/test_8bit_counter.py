# (c) OctopusLAB 2017-25 - MIT

from time import sleep_ms
from machine import Pin

# D0_D7
led_pins = [14, 48, 3, 16, 15, 9, 47, 21]
leds = [Pin(p, Pin.OUT) for p in led_pins]

# ---------------
def clear_all():
    for led in leds:
        led.value(0)

def snake(delay=150):
    """Rozsvěcování LEDek postupně"""
    for i in range(len(leds)):
        clear_all()
        leds[i].value(1)
        sleep_ms(delay)
    clear_all()

def counter(delay=200):
    """Čítač 0–255 v binární podobě na LEDkách"""
    for num in range(256):
        for i in range(8):
            bit = (num >> i) & 1   # vezmi i-tý bit
            leds[i].value(bit)
        sleep_ms(delay)

# ========== main ==========
while True:
    for a in range(5):
       snake(120) 
       
    counter(100) 
