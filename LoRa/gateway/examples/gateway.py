from time import sleep
from mqtt import MQTTClient
import json
import network
import config

class Sensor:
    def __init__(self):
        return

    nodes = ['Node_1', 'Node_2', 'Node_3', 'Node_4', 'Node_5']
    zones = ['1']
    client = MQTTClient(config.mqtt_config['mqtt_uid'], config.mqtt_config['mqtt_server'], user=config.mqtt_config['mqtt_user'], password=config.mqtt_config['mqtt_pass'], port=config.mqtt_config['mqtt_port'])
    
    def sub_cb(topic, msg):
       print(msg)
    
    def do_connect():
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        if not wlan.isconnected():
            print('connecting to network...')
            wlan.connect(config.wifi_config['ssid'], config.wifi_config['password'])
            while not wlan.isconnected():
                pass
            
    def mqtt_sub():
        for i in Sensor.zones:
            z = i
            for i in Sensor.nodes:
                n = i
                Sensor.client.subscribe(topic=f'Zone{z}/{n}')
    
    def mqtt_pub(payload):
        for n in Sensor.nodes:
            if n in payload:
                for z in Sensor.zones:
                    if z in payload:
                        Sensor.client.publish(topic=f'Zone{z}/{n}', msg=payload, qos=1)