#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# CamJam EduKit 3 - Robotics
# Worksheet 3 – Driving and Turning

#edited by @AndreasKopp http:/www.erfindergarden.de

import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setze die Variablen für die Motorpins
# das sind deine Pins beim Cam Jam Edu Board
# beim Ryanteck Board sind sie 17, 18 und 22 und 23
# beim RaspiRobot Board sind sie 17, 14 und 10 und 25
# beim Explorer Hat Pro sind sie 19, 20 und 21, 26

# wenn du ein anderes Board hast ales das Cam Jam Board schreibe deine Pins rein


pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 8
pinMotorBBackwards = 7

# Set the GPIO Pin mode
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)

# Turn all motors off
def Stop():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 0)
    
# Turn both motors forwards
def Vorwaerts():
    GPIO.output(pinMotorAForwards, 1)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 1)
    GPIO.output(pinMotorBBackwards, 0)
    
# Turn both motors backwards
def Backwards():
	GPIO.output(pinMotorAForwards, 0)
	GPIO.output(pinMotorABackwards, 1)
	GPIO.output(pinMotorBForwards, 0)
	GPIO.output(pinMotorBBackwards, 1)
	
# Turn left
def Links():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 1)
    GPIO.output(pinMotorBForwards, 1)
    GPIO.output(pinMotorBBackwards, 0)
    
# Turn Right
def Rechts():
    GPIO.output(pinMotorAForwards, 1)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 1)



Rechts()
time.sleep(10)
Stop()
GPIO.cleanup()
