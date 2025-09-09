# esp32_s3_robotics
Basic experiments with the ESP32-S3 development board focused on IoT, robotics, and electronics fundamentals — mostly using MicroPython.

---

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
