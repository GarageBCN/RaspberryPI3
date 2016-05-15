# RaspberryPi3

RaspberryPi3 Preliminary testing

## Introduction

During the May 14th to 15th hackathon, we started working on having Python in RaspberryPi3 able to use GPIO, and the code running on Docker.

## RaspberryPi3 setup

TODO

## Wiring for testing

Put a LED and a button on the breadboard, then, connect the following:

- GPIO 17 to LED.
- GPIO 27 to button with a pull down resistor.

## Run the testing

Run the following commands on RaspberryPi3:

    git clone https://github.com/GarageBCN/RaspberryPi3
    cd RaspberryPi3
    bash launch
    
Once this returned the container hash, the button would act as a switch to light on and off the LED.
For stopping the container, use the following command:

    bash stop
