# RaspberryPi3

RaspberryPi3 Preliminary testing

## Introduction

During the May 14th to 15th hackathon, we started working on having Python in RaspberryPi3 able to use GPIO, and the code running on Docker.

## RaspberryPi3 setup

First, on a fresh [Raspbian latest](https://downloads.raspberrypi.org/raspbian_latest) install, setup docker:

    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install -y apt-transport-https
    wget -q https://packagecloud.io/gpg.key -O - | sudo apt-key add -
    echo 'deb https://packagecloud.io/Hypriot/Schatzkiste/debian/ wheezy main' | sudo tee /etc/apt/sources.list.d/hypriot.list
    sudo apt-get update
    sudo apt-get install -y docker-hypriot
    sudo systemctl enable docker
    sudo service docker start
    
To check docker is ok, do the following commands:

    sudo service docker status
    sudo docker ps
    
The first command output should state the docker daemon is `active (running)`, and the second command output should just print an empty table with headers, saying `CONTAINER ID      IMAGE...`.

## Wiring for testing

Put a LED and a button on the breadboard, then, connect the following:

- GPIO 17 to LED.
- GPIO 27 to button with a pull down resistor.

## Run the testing

Run the following commands on RaspberryPi3:

    git clone https://github.com/GarageBCN/RaspberryPi3
    cd RaspberryPi3
    sudo bash launch
    
Once this returned the container hash, the button would act as a switch to light on and off the LED.
For stopping the container, use the following command:

    sudo bash stop
