#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Mit diesem Programm testen wir den Ultraschallsensor und geben
#  dafür den berechneten Abstand eines Objekts vor dem Sensor aus.
#
#  Dieses Programm ist Bestandteil des Erfindergarden Roboter-Workshops.
#  http://www.erfindergarden.de

from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=18, trigger=17)
while True:
 print('Distance: ', sensor.distance * 100)
 sleep(1)
