#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Mit diesem Programm testen wir den Infrarotsensor und geben
#  dafür aus, ob er gerade weiß oder schwarz sieht.
#
#  Dieses Programm ist Bestandteil des Erfindergarden Roboter-Workshops.
#  http://www.erfindergarden.de

import time
import gpiozero

sensor = gpiozero.LineSensor(25)	# Unser Sensor ist am Pin 25 angeschlossen

def black():
	print("Ich sehe schwarz")

def white():
	print("Ich sehe weiß")

sensor.when_line = black
sensor.when_no_line = white
