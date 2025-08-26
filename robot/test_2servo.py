from machine import Pin, PWM
from time import sleep

servo1 = PWM(Pin(21), freq=50)  # P1
servo2 = PWM(Pin(47), freq=50)  # P2

def set_servo1_speed(percent):
    # percent: -100 až 100
    # -100 = max otáčení jedním směrem
    # 0 = stop
    # 100 = max otáčení opačným směrem
    # mapujeme na ms: 1ms → -100%, 1.5ms → 0%, 2ms → +100%
    ms = 1.5 + (percent / 200)  # -100 → 1ms, 100 → 2ms
    servo1.duty_ns(int(ms * 1_000_000))
    
def set_servo2_speed(percent):
    # percent: -100 až 100
    # -100 = max otáčení jedním směrem
    # 0 = stop
    # 100 = max otáčení opačným směrem
    # mapujeme na ms: 1ms → -100%, 1.5ms → 0%, 2ms → +100%
    ms = 1.5 + (percent / 200)  # -100 → 1ms, 100 → 2ms
    servo2.duty_ns(int(ms * 1_000_000))
    
i = 0

while True:
    print(i)
    i = i+1
    set_servo1_speed(-50)
    set_servo2_speed(50)
    sleep(2)
    set_servo1_speed(-100)
    set_servo2_speed(100)   # forw
    sleep(5)
    set_servo1_speed(0)
    set_servo2_speed(0)
    sleep(3)
    set_servo1_speed(-100) # otáčí opačně plnou rychlostí
    sleep(2)
    set_servo1_speed(0)    # stop
    sleep(2)
    for s in range(0,10):
        set_servo2_speed(s*10)
        sleep(0.5)
    set_servo2_speed(0)
    sleep(3)
        
