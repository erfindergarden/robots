#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Mit diesem Programm testen wir ob die Motoren korrekt funktionieren.
#
#  Beim Aufruf sollten sich beide Motoren für eine Sekunde vorwärts drehen.
#  Wenn sie sich gar nicht drehen, sind die Motoren, das Batteriepack oder
#  das Board nicht korrekt angeschlossen oder defekt.
#
#  Wenn sich ein Motor in die falsche Richtung dreht, muss er umgepolt,
#  d.h. die beiden Kabel vertauscht werden.
#
#  Dieses Programm ist Bestandteil des Erfindergarden Roboter-Workshops.
#  http://www.erfindergarden.de

import RPi.GPIO as GPIO		# Diese Library ermöglicht es uns, die GPIO-Pins zu steuern

import time					# Hiermit können wir den Ablauf unseres Programms pausieren.
							# Das wird später benötigt um zu bestimmen, wie
							# lange die Motoren laufen sollen.

GPIO.setmode(GPIO.BCM)		# Wir verwenden das BCM-System zur Nummerierung der Pins
GPIO.setwarnings(False)		# Warnungen werden unterdrückt

# Alle benötigten Pins als Outputs definieren
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

# Rechter Motor vorwärts
GPIO.output(9, 0)
GPIO.output(10, 1)

# Linker Motor vorwärts
GPIO.output(7, 0)
GPIO.output(8, 1)

# Die Motoren sollen eine Sekunde laufen und dann stoppen
time.sleep(1)	# 1 Sekunde warten
GPIO.cleanup()  # Alle Pins ausschalten
