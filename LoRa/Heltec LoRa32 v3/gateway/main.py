from lib.sx1262 import SX1262
from lib.ssd1306 import SSD1306_I2C
import time
from machine import Pin, SoftI2C
from gateway import Gateway
import ujson as json

sx = SX1262(spi_bus=2, clk=9, mosi=10, miso=11, cs=8, irq=14, rst=12, gpio=13)
oledSDA = Pin(18, Pin.OUT, Pin.PULL_UP)
oledSCL = Pin(17, Pin.OUT, Pin.PULL_UP)
oledRST = Pin(21, Pin.OUT, Pin.PULL_UP)
oledRST.value(1)
i2c = SoftI2C(oledSDA, oledSCL)
oled = SSD1306_I2C(128, 64, i2c)
count = 0

# LoRa
sx.begin(freq=915, bw=500.0, sf=12, cr=8, syncWord=0x12,
         power=-5, currentLimit=60.0, preambleLength=8,
         implicit=False, implicitLen=0xFF,
         crcOn=True, txIq=False, rxIq=False,
         tcxoVoltage=1.7, useRegulatorLDO=False, blocking=True)

# FSK
##sx.beginFSK(freq=923, br=48.0, freqDev=50.0, rxBw=156.2, power=-5, currentLimit=60.0,
##            preambleLength=16, dataShaping=0.5, syncWord=[0x2D, 0x01], syncBitsLength=16,
##            addrFilter=SX126X_GFSK_ADDRESS_FILT_OFF, addr=0x00, crcLength=2, crcInitial=0x1D0F, crcPolynomial=0x1021,
##            crcInverted=True, whiteningOn=True, whiteningInitial=0x0100,
##            fixedPacketLength=False, packetLength=0xFF, preambleDetectorLength=SX126X_GFSK_PREAMBLE_DETECT_16,
##            tcxoVoltage=1.6, useRegulatorLDO=False,
##            blocking=True)

Gateway.do_connect()

while True:
    msg, err = sx.recv()
    if len(msg) > 0:
        error = SX1262.STATUS[err]
        payload = json.loads(msg.decode('utf-8'))
        count+=1
        oled.fill(0)
        oled.text(f'MSG RECEIVED:', 0, 0)
        oled.text(f'{count}', 0, 10)
        oled.show()
        if "Node_1" in payload:
            Gateway.client.set_callback(Gateway.sub_cb)
            Gateway.client.connect()
            Gateway.mqtt_sub('Node_1')
            Gateway.mqtt_pub('Node_1', payload)
            Gateway.client.disconnect()
        elif "Node_2" in payload:
            Gateway.client.set_callback(Gateway.sub_cb)
            Gateway.client.connect()
            Gateway.mqtt_sub('Node_2')
            Gateway.mqtt_pub('Node_2', payload)
            Gateway.client.disconnect()
        elif "Node_3" in payload:
            Gateway.client.set_callback(Gateway.sub_cb)
            Gateway.client.connect()
            Gateway.mqtt_sub('Node_3')
            Gateway.mqtt_pub('Node_3', payload)
            Gateway.client.disconnect()
        elif "Node_4" in payload:
            Gateway.client.set_callback(Gateway.sub_cb)
            Gateway.client.connect()
            Gateway.mqtt_sub('Node_4')
            Gateway.mqtt_pub('Node_4', payload)
            Gateway.client.disconnect()
        print(payload)
        print(error)
