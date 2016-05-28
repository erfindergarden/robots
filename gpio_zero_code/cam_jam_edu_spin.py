from gpiozero import CamJamKitRobot
from time import sleep

robot = CamJamKitRobot()

robot.left()
sleep(5)
robot.stop()
robot.backward()
sleep(5)
robot.right()
sleep(5)
robot.reverse()
robot.forward(0.5)
sleep(5)
robot.stop()
                                                                                                                                                                                                                                      