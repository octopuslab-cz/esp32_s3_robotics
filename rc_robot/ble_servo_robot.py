# octopusLAB - Micropython v1.20-23
# | BLE test | BlueFruit or Dabble mobile app.

from machine import Pin, PWM
from lib.octopus_lib import getUid
from time import sleep
from components.led import Led

print("BLE init")
from utils.ble import bleuart
import utils.ble.bluefruit as bf

servo1 = PWM(Pin(21), freq=50)  # P1
servo2 = PWM(Pin(47), freq=50)  # P2

def set_servo1_speed(percent):
    # percent: -100 až 100
    # -100 = max otáčení jedním směrem
    # 0 = stop
    # 100 = max otáčení opačným směrem
    # mapujeme na ms: 1ms → -100%, 1.5ms → 0%, 2ms → +100%
    ms = 1.5 + (percent / 100)  # -100 → 1ms, 100 → 2ms
    servo1.duty_ns(int(ms * 1_000_000))
    
def set_servo2_speed(percent):
    ms = 1.5 + (percent / 100)  # -100 → 1ms, 100 → 2ms
    servo2.duty_ns(int(ms * 1_000_000))


uID5 = getUid(short=5)

led = Led(39)
print("---> BLE and BlueFruit mobile app. - led")
print("This is simple Micropython example | ESP32 & octopusLAB")

speed = 800

led.blink()
sleep(2)
led.blink()


def on_data_received(connection, data):
    print("data: ",str(data))
    
    # --- BlueFruit app.
    if data == bf.UP:
        print("Up")
        set_servo2_speed(100)
        set_servo1_speed(-100)
        led.value(1)
    if data == bf.DOWN:
        print("Down")
        led.value(0)
        set_servo1_speed(0)
        set_servo2_speed(0)
    if data == bf.LEFT:
        print("Left")
        set_servo2_speed(100)
    if data == bf.RIGHT:
        print("Right")
        set_servo1_speed(-100)

    sleep(0.2)
    
    # --- Dabble app.   
    if len(data) == 8 and data[4] == 2:
        if data[6] & 0x01 << 0:    # UP:   b'\xff\x01\x01\x01\x02\x00\x00\x00'
            print("up")
            set_servo2_speed(100)
            set_servo1_speed(-100)
        elif data[6] & 0x01 << 1:  # Down  b'\xff\x01\x01\x01\x02\x00\x02\x00'
            print("down")
            set_servo2_speed(0)
            set_servo1_speed(0)
        elif data[6] & 0x01 << 2:  # Left  b'\xff\x01\x01\x01\x02\x00\x04\x00'
            print("left")
            set_servo2_speed(100)
        elif data[6] & 0x01 << 3:  # right b'\xff\x01\x01\x01\x02\x00\x08\x00'
            print("rigt")
            set_servo1_speed(-100)
            
        elif data[5] & 0x01 << 2:  # tri.  b'\xff\x01\x01\x01\x02\x04\x00\x00'
            print("triangle")
        elif data[5] & 0x01 << 3:
            print("circle")
        else:
            print("no other bits, Data received: ", data)
    else:
        print("Data received: ", data) 
    
    
    
devName = 'octopus-test-'+uID5
print("BLE ESP32 device name: " + devName)
print("="*32)

uart = bleuart.BLEUART(name=devName, on_data_received=on_data_received)
uart.start()

while True:
    sleep(0.1)