# mip_install.py # install octopusLAB framework 2

from time import sleep
import network
import mip

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
sleep(5)

print("wifi connect")
wlan.connect(YOUR_SSID, YOUR_PASSW)
sleep(5)

# mip.install("github:octopuslab-cz/esp32_micropython_framework/package_min.json", target=".")
mip.install("github:octopuslab-cz/esp32_micropython_framework/package_ble.json", target=".")