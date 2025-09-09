# esp32_s3_robotics

Basic experiments with the ESP32-S3 development board focused on IoT, robotics, and electronics fundamentals — mostly using MicroPython.

After ten years of experimenting and development, we are introducing a new **universal module** for robotics and programming.  
At its core is the modern **ESP32-S3 controller**, combined with a **power management module** (including built-in Li-Ion battery charging).  

The board connects via **USB-C**, which is used for programming, testing, and also for charging the battery.


## Features

- Sufficient number of GPIO pins  
- Two built-in LEDs (connected via jumpers)  
- Two RGB LEDs  
- Integrated accelerometer and gyroscope module  
- Direct connection for up to eight servo motors 

---

### **Main Technical Specifications**

* **Microcontroller:** ESP32-S3 WROOM-1
* **Connectivity:** 2.4 GHz Wi-Fi (802.11 b/g/n) and Bluetooth 5.0 (LE)
* **Dimensions:** 68 mm x 50 mm
* **Power Supply:** 
    * **USB-C connector:** For power and programming. Power can be controlled via a switch.
    * **Battery:** Battery connection (Li-ion/Li-pol) via jumper.
* **Charging Circuit:** **TP4056** with a charging current of **270 mA**
    * **Charging Status Indication:** Bi-color LED
        * **Red:** Charging
        * **Green:** Charging complete
        * **Green - blinking:** Battery not connected
 

---

## GPIO Pinout

```

SPI_CLK_PIN:  12
SPI_MOSI_PIN: 11
I2C_SCL_PIN:   2
I2C_SDA_PIN:   1
BUTT0_PIN:     0
SPI_MISO_PIN: 13
SPI_CS0_PIN:  10

P1_PIN:  21
P2_PIN:  47
P3_PIN:   9
P4_PIN:  15
P5_PIN:  16
P6_PIN:   3
P7_PIN:  48
P8_PIN:  14
BATMES_PIN: 5

PWM1_PIN: 21
PWM2_PIN: 47
PWM3_PIN:  9

LED1_PIN: 14
LED2_PIN: 48
WSLED_PIN: 38

D1_PIN: 16
D2_PIN: 15
D3_PIN:  3

RXD1: 18
TXD1: 17
RXD0: 20
TXD0: 21


```




This project is based on the octopusLab [esp32_micropython_framework](https://github.com/octopuslab-cz/esp32_micropython_framework)


---

Installing the **OctopusLAB framework** is quick and easy using **mip**:

```Python
# mip_install.py # install octopusLAB framework 2

from time import sleep
import network
import mip

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
sleep(5)

wlan.connect('ssid', 'password')
sleep(5)

mip.install("github:octopuslab-cz/esp32_micropython_framework/package.json", target=".")
```
---
