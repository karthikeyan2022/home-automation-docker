import paho.mqtt.publish as publish
import time
import RPi.GPIO as GPIO

import netifaces as ni
ni.ifaddresses('wlan0')
ip = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']

connect = 29
sense = 32
GPIO.setmode(GPIO.BOARD)
GPIO.setup(connect,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(sense, GPIO.IN)

MQTT_SERVER = ip
MQTT_PATH = '/ldr'

MQTT_CLIENT_ID = 'ldr-'



if __name__ == '__main__':
    try:
        while True:
            value="Light OFF"
            if GPIO.input(sense):
                print "Light ON"
                value = "Light ON"
            else:
                print "Light OFF"
		value = "Light OFF"
            #time.sleep(0.5)
            if GPIO.input(connect) == False:
              print "publishing"
              publish.single(MQTT_PATH, value, hostname=MQTT_SERVER)
            else:
              value="device unplugged"
              publish.single(MQTT_PATH,value, hostname=MQTT_SERVER)

    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
