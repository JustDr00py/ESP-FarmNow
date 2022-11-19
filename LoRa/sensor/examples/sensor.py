import network, ubinascii, espnow, onewire, time, ds18x20, json
from machine import Pin, deepsleep
from time import sleep, sleep_ms
import config

class Sensor:
    #CHANGE THESE SETTINGS
    tempsensor = Pin(13, Pin.IN)
    ow = onewire.OneWire(tempsensor)
    ds = ds18x20.DS18X20(ow)    
    
    def get_data():
        node = {}
        node["Zone"] = config.sensor_config['zone']
        node["ID"] = config.sensor_config['uid']
        node["Temperature"] = Sensor.get_temp()
        return node

    def get_temp():
        roms = Sensor.ds.scan()
        #print(roms)
        Sensor.ds.convert_temp()
        sleep_ms(750)
        for rom in roms:
            temp = Sensor.ds.read_temp(rom) * 1.8 + 32
            return f'{temp:.2f}'

    def send_temp():
        payload = json.dumps(f'{Sensor.get_data()}')
        print(payload)
        return payload
    