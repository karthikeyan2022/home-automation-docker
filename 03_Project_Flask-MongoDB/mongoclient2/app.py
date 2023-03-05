import time
import RPi.GPIO as GPIO
from pymongo import MongoClient

connect = 38
sense = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(connect,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(sense, GPIO.IN)

client = MongoClient("mongodb+srv://raspberrypi_docker_user:raspberrypi@cluster0-tgb3y.mongodb.net/test?retryWrites=true")

db = client.project
collection = db.sensors
#collection.insert_one( { "id": 2, "name": "moisture", "value": "water detected" } )
#collection.update_one( {"id": 1 }, { "$set": { "value": "53" } } )

  


if __name__ == '__main__':
  while True:
      try:
          value="Water not detected"
          if GPIO.input(sense):
              print "No Water Detected!"
              value = "Water not detected"
          else:
              print "Water Detected!"
              value = "Water detected"
          if GPIO.input(connect) == False:
              print (value)
              collection.update_one( {"id": 2 }, { "$set": { "value": value } } )
              time.sleep(1)
          else:
              value="device unplugged"
              collection.update_one( {"id": 2 }, { "$set": { "value": value } } )
              time.sleep(1)

      # Reset by pressing CTRL + C
      except KeyboardInterrupt:
          print("Measurement stopped by User")
          GPIO.cleanup() 
