import time
import RPi.GPIO as GPIO
from smbus2 import SMBus
from pymongo import MongoClient


connect = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(connect,GPIO.IN, pull_up_down=GPIO.PUD_UP)

# By default the address of LM75A is set to 0x48
# aka A0, A1, and A2 are set to GND (0v).
address = 0x48


client = MongoClient("mongodb+srv://raspberrypi_docker_user:raspberrypi@cluster0-tgb3y.mongodb.net/test?retryWrites=true")

db = client.project
collection = db.sensors
#collection.insert_one( { "id": 2, "name": "moisture", "value": "water detected" } )
#collection.update_one( {"id": 1 }, { "$set": { "value": "53" } } )

bus = SMBus(1)
    


if __name__ == '__main__':
  while True:
      try:
          raw = bus.read_word_data(address, 0) & 0xFFFF
          raw = ((raw << 8) & 0xFF00) + (raw >> 8)
          temperature = (raw / 32.0) / 8.0
          if GPIO.input(connect) == False:
            print (temperature)
            collection.update_one( {"id": 1 }, { "$set": { "value": temperature } } )
            time.sleep(1)
          else:
            value="device unplugged"
            collection.update_one( {"id": 1 }, { "$set": { "value": value } } )
            time.sleep(1)

      except Exception as e:
          print("failed to establish connection")
          collection.update_one( {"id": 1 }, { "$set": { "value": "device unplugged" } } )
          time.sleep(1)
 