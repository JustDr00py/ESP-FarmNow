from mqtt import MQTTClient
import network, config


class Gateway:
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
            
    def mqtt_sub(topic):
        Gateway.client.subscribe(topic=topic)
                
    
    def mqtt_pub(topic, payload,):
        Gateway.client.publish(topic=topic, msg=payload, qos=1)