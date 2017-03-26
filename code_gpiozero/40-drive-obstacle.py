import gpiozero
import time

robot = gpiozero.CamJamKitRobot()
sensor = gpiozero.DistanceSensor(18, 17)

speed = 0.2
min_distance = 0.25 # m

def avoid():
	print("Avoiding obstacle.")
	robot.left(speed)
	time.sleep(0.2)

try:
	while True:
		if sensor.distance < min_distance:
			avoid()
		else:
			robot.forward(speed)
		time.sleep(0.1)
except KeyboardInterrupt:
	robot.stop()