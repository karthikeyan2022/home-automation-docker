# home-automation-docker

Project: Design and Implementation of Microservices Architecture for home Automation

![This is an image](/assets/images/block_diagram.svg)

## Project overview

The sensors will send the data to the raspberry pi. The raspberry pi will send the data to the API Gateway where the Api Gateway should be used with Docker, in which the REST architecture is used ( in which each sensor and database will have a container), then the Api gateway should find the appropriate service for them in service layer, (Device monitoring, Device configuration, Device management, Notification service should be  created in such a way that it should monitor the entire system from outside ).
The main motto of this project is if someone update the code for one sensor or if one sensor is not working also, it should not affect the service of another sensor.
