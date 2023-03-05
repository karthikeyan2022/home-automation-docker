import paho.mqtt.publish as publish
import time
import RPi.GPIO as GPIO
from smbus2 import SMBus

import netifaces as ni
ni.ifaddresses('wlan0')
ip = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
connect = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(connect,GPIO.IN, pull_up_down=GPIO.PUD_UP)

# By default the address of LM75A is set to 0x48
# aka A0, A1, and A2 are set to GND (0v).
address = 0x48

MQTT_SERVER = ip
MQTT_PATH = '/temperature'

MQTT_CLIENT_ID = 'temp'

bus = SMBus(1)

if __name__ == '__main__':
    while True:
        try:
            raw = bus.read_word_data(address, 0) & 0xFFFF
            raw = ((raw << 8) & 0xFF00) + (raw >> 8)
            temperature = (raw / 32.0) / 8.0
            time.sleep(1)

            # publish to mqtt server
            if GPIO.input(connect) == False:
                print (temperature)
                publish.single(MQTT_PATH, temperature, hostname=MQTT_SERVER)
            else:
                value="device unplugged"
                publish.single(MQTT_PATH, value, hostname=MQTT_SERVER)

        except Exception as e:
            print("failed to establish connection")
            publish.single(MQTT_PATH, "Device unplugged", hostname=MQTT_SERVER)
 
