#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Mit diesem Programm testen wir erneut ob die Motoren korrekt funktionieren
#  und verwenden dafür die "gpiozero" library.
#
#  Dieses Programm ist Bestandteil des Erfindergarden Roboter-Workshops.
#  http://www.erfindergarden.de

import gpiozero				# Eine Abstraktion der GPIO, die Funktionen
							# zur Steuerung der Motoren enthält

import time					# Hiermit können wir den Ablauf unseres Programms pausieren.
							# Das wird später benötigt um zu bestimmen, wie
							# lange die Motoren laufen sollen.

robot = gpiozero.Robot(left = (9, 10), right = (7, 8))	# Hier sagen wir gpiozero an welche Pins
														# unsere Motoren angeschlossen sind

robot.forward()				# gpiozero stellt nun im Hintergrund die Pins 8 und 10 auf 1
							# und die Pins 7 und 9 auf 0, genau wie im vorigen Motor-Test.
							# Nur ist dieser Code hier wesentlich besser "lesbar".

time.sleep(1)				# Warte eine Sekunde
robot.stop()				# gpiozero stellt alle vier Pins der Motoren auf 0
