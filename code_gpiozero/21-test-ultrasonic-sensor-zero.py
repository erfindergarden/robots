#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Mit diesem Programm testen wir den Ultraschallsensor und geben
#  dafür den berechneten Abstand eines Objekts vor dem Sensor aus.
#
#  Dieses Programm ist Bestandteil des Erfindergarden Roboter-Workshops.
#  http://www.erfindergarden.de

import time
import gpiozero

sensor = gpiozero.DistanceSensor(18, 17)	# Unser Sensor ist an den Pins 17 und 18 angeschlossen

while True:  # Wiederhole den folgenden Codeblock unendlich
	print "Abstand vor dem Sensor: %f cm" % sensor.distance*100
	time.sleep(1)  # Warte eine Sekunde vor der nächsten Ausgabe
