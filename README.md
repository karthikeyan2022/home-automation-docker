# home-automation-docker

Project: Design and Implementation of Microservices Architecture for home Automation

![This is an image](/assets/images/block_diagram.svg)

## Project overview

The sensors will send the data to the raspberry pi. The raspberry pi will send the data to the API Gateway where the Api Gateway should be used with Docker, in which the REST architecture is used ( in which each sensor and database will have a container), then the Api gateway should find the appropriate service for them in service layer, (Device monitoring, Device configuration, Device management, Notification service should be  created in such a way that it should monitor the entire system from outside ).
The main motto of this project is if someone update the code for one sensor or if one sensor is not working also, it should not affect the service of another sensor.

## INSTRUCTIONS

### For graphical display of raspberry pi to a laptop or PC using VNC viewer (wirelessly)

 1. Enable VNC in raspberry pi using raspi-config

 2. Configure a WiFi network for connecting to Raspberry Pi. Go to /etc/wpa_supplicant and edit the wpa_supplicant.conf file. Add a ssid and password entry in that file.

 3. In PC or laptop, using VNC viewer enter the IP address of raspberry pi connected to the same wifi.

### Running the docker project (Flask-Mongodb-REST)

METHOD 1: Docker compose

  1. Go to the Desktop directory "cd Desktop"
  2. Run the command "sudo docker-compose up -d"  
(refer docker-compose.yml file in that directory which starts the docker containers)

METHOD 2: Running the Docker containers separately

  1. Refer DOCKER COMMANDS for building and running docker containers
  2. Run the following commands:
`sudo docker run -d -p 5000:5000 flaskmongo`\
`sudo docker run --privileged -d mongoclient1`\
`sudo docker run --privileged -d mongoclient2`\
`sudo docker run --privileged -d mongoclient3`\

## Running the docker project (MQTT-NGINX)

METHOD 1: Docker compose

  1. Go to the directory that contains corresponding docker-compose.yml ( in /home/pi/Documents/dockercompose_files/mqttserver
  2. Run the command "sudo docker-compose up -d"
(refer docker-compose.yml file in that directory which starts the docker containers)

METHOD 2: Running the Docker containers seperately

  1. Download the docker images mbixtech/arm32v7-mosquitto and tobi312/rpi-nginx (Refer DOCKER COMMANDS)
  2. Refer DOCKER COMMANDS for building and running docker containers
  3. Run the following commands:

  (Refer to the directory /home/pi/.config/mosquitto/mosquitto.conf)
  `sudo docker run -d -p 1883:1883 -p 9001:9001 -v /home/pi/.config/mosquitto/mosquitto.conf:/mosquitto/config/mosquitto.conf mbixtech/arm32v7-mosquitto`\

  (Ensure SPI is enabled. Enable it by running "sudo raspi-config")
"sudo docker run --network="host" --privileged -d temperature-service"

"sudo docker run --network="host" --privileged -d moisture-service"

"sudo docker run --network="host" --privileged -d ldr-service"

(modify the index.html file located at /home/pi/html changing the mqtt server address)
(Refer to the directory /home/pi/.config/nginx and /home/pi/html )
"sudo docker run -d -p 80:80 -v /home/pi/.config/nginx:/etc/nginx/conf.d:ro -v /home/pi/html:/var/www/html tobi312/rpi-nginx"

## DOCKER COMMANDS

 1. Building a docker image:
Create a directory
Create a Dockerfile in that directory that conains instructions for building a docker image.
The required app.py file is included in the directory.
requirements.txt file contains the names of dependencies to be downloaded ( to be refered in Dockerfile )
Run the following command for building the image ( ensure '.' character is included)
`sudo docker build -t container-name .`\
For Example: `sudo docker build -t temperature-service .`\

 2. Command for checking the running containers
`sudo docker container ls`\

 3. Command for stopping the running containers
`sudo docker container stop $(sudo docker container ls -q)`\

 4. Command for downloading a docker image
`sudo docker pull image-name`\

## REFERENCES

  <https://www.instructables.com/id/Measuring-Temperature-With-I2C-Sensor-LM75A-on-Ras/>
  <https://www.instructables.com/id/Soil-Moisture-Sensor-Raspberry-Pi/>
  <https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask>
  <https://linuxize.com/post/how-to-remove-docker-images-containers-volumes-and-networks/>
  <https://hub.docker.com/r/mbixtech/arm32v7-mosquitto/>
  <http://nilhcem.com/iot/home-monitoring-with-mqtt-influxdb-grafana>
  <https://www.berthon.eu/2019/revisiting-getting-docker-compose-on-raspberry-pi-arm-the-easy-way/>
  <https://www.eclipse.org/paho/clients/js/>
