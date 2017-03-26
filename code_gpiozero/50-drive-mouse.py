import gpiozero
import time
from pynput import mouse

ROTATE_SPEED = .3

robot = gpiozero.CamJamKitRobot()
speed = 0.0
direction = None

def onClick(x, y, button, pressed):
	global direction
	if not pressed:
		direction = None
	elif button == mouse.Button.left:
		direction = 'left'
	elif button == mouse.Button.right:
		direction = 'right'

def onScroll(x, y, dx, dy):
	global speed
	speed = min([1, max([0, speed + float(dy)/100])])
	print 'new speed: %f' % speed

# Register mouse events
thread = mouse.Listener(on_click=onClick, on_scroll=onScroll)
thread.start()

try:
	print 'Starting robot'
	while True:
		if direction is None:
			robot.forward(speed)
		elif direction == 'left':
			robot.left(ROTATE_SPEED)
		elif direction == 'right':
			robot.right(ROTATE_SPEED)

		time.sleep(0.1)

except KeyboardInterrupt:
	robot.stop()