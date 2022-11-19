from machine import Pin, SoftI2C
from ssd1306 import SSD1306_I2C
from time import sleep
from examples.sensor import Sensor

#Remove comment for OLED
"""
oledSDA = Pin(15, Pin.OUT, Pin.PULL_UP)
oledSCL = Pin(4, Pin.OUT, Pin.PULL_UP)
oledRST = Pin(16, Pin.OUT)
oledRST.value(1)
i2c = SoftI2C(oledSDA, oledSCL)
oled = SSD1306_I2C(128, 64, i2c)
"""

def send(lora):
    print("LoRa Sender")

    while True:
        payload = f'{Sensor.send_temp()}'
        #print(f"Sending packet: \n{payload}\n") #Used for serial debug.
        lora.println(payload)
        sleep(10)
        
        #Remove comment for OLED
        """
        oled.fill(0)
        oled.text('Sending packet:' , 0, 0)
        oled.text(f'{payload}' , 0, 10)
        oled.show()
        """
        
