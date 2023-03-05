# USING MOSQUITTO FOR THE PROJECT ( temperature-sensor, moisture-sensor, ldr-sensor )

## Prerequisites

1. Install docker
Update and install docker
`sudo apt-get update && sudo apt-get upgrade` \
`curl -fsSL https://get.docker.com -o get-docker.sh` \
`sudo sh get-docker.sh`

Add docker to group and refresh (log out or reboot)
`sudo usermod -aG docker pi`

Verify the installation
`docker run hello-world`
 <https://www.simplilearn.com/tutorials/docker-tutorial/raspberry-pi-docker>

2. Enable SPI in sudo raspi-config
Interface options -> SPI

3. Copy mosquitto and nginx folders to /home/pi/.config

## Build and running the project

1. Build each service using the command (respective folder)
`sudo docker build -t temperature-service .`

2. Run mosquitto mqtt broker service. mosquitto.conf is volume mapped
`sudo docker run -d -p 1883:1883 -p 9001:9001 -v /home/pi/.config/mosquitto/mosquitto.conf:/mosquitto/config/mosquitto.conf mbixtech/arm32v7-mosquitto`

3. Run all the sensor services
`sudo docker run --network="host" --privileged -d temperature-service` \
`sudo docker run --network="host" --privileged -d moisture-service` \
`sudo docker run --network="host" --privileged -d ldr-service`

3. Run the nginx server now
Modify the index.html file located at /home/pi/html for changing the mqtt server address
The nginx directory contains default.conf
`sudo docker run -d -p 80:80 -v /home/pi/.config/nginx:/etc/nginx/conf.d:ro -v /home/pi/html:/var/www/html arm32v7/nginx`

`sudo docker run -d -p 80:80 -v /home/pi/.config/nginx:/etc/nginx/conf.d:ro -v /home/pi/html:/var/www/html tobi312/rpi-nginx` <--(removed)

## Useful commands (docker, linux)

To remove dangling docker images:
`sudo docker image prune`

To access network interfaces (netifaces python library)
`--network="host"`

To stop all the containers
`sudo docker container stop $(docker container ls -aq)`

To update restart policy
`docker update --restart=no my-container`
