# Simple two DC motor robot class usage example.
# Author: Tony DiCola
# License: MIT License https://opensource.org/licenses/MIT
import time

# Import the Robot.py file (must be in the same directory as this file!).
import Robot


# Set the trim offset for each motor (left and right).  This is a value that
# will offset the speed of movement of each motor in order to make them both
# move at the same desired speed.  Because there's no feedback the robot doesn't
# know how fast each motor is spinning and the robot can pull to a side if one
# motor spins faster than the other motor.  To determine the trim values move the
# robot forward slowly (around 100 speed) and watch if it veers to the left or
# right.  If it veers left then the _right_ motor is spinning faster so try
# setting RIGHT_TRIM to a small negative value, like -5, to slow down the right
# motor.  Likewise if it veers right then adjust the _left_ motor trim to a small
# negative value.  Increase or decrease the trim value until the bot moves
# straight forward/backward.
LEFT_TRIM   = 0
RIGHT_TRIM  = 0


# Create an instance of the robot with the specified trim values.
# Not shown are other optional parameters:
#  - addr: The I2C address of the motor HAT, default is 0x60.
#  - left_id: The ID of the left motor, default is 1.
#  - right_id: The ID of the right motor, default is 2.
robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)

# Now move the robot around!
# Each call below takes two parameters:
#  - speed: The speed of the movement, a value from 0-255.  The higher the value
#           the faster the movement.  You need to start with a value around 100
#           to get enough torque to move the robot.
#  - time (seconds):  Amount of time to perform the movement.  After moving for
#                     this amount of seconds the robot will stop.  This parameter
#                     is optional and if not specified the robot will start moving
#                     forever.


#######################################################################
##This is where we edit in the way the car should move
#All other code created by Adafruit
############################################################################

def SolvePath(path, di):
	for s in path:
		if (s == 'u'):
			up()
		if (s == 'r'):
			right()
		if (s == 'd'):
			down()
		if (s == 'l'):
			left()

def up():
	if (getDirection() == 1):
		robot.left(50,0.5)	#Turn left 90 degrees
	if (getDirection() == 2):
		robot.right(50,1.0)	#Turn right 180 degrees	
	if (getDirection() == 3):
		robot.right(50,0.5)	#Turn right 90 degrees
	robot.forward(50, 1.0)
	setDirection(0)


def right():
	if (getDirection() == 0):
		robot.right(50,0.5)	#Turn right 90 degrees
	if (getDirection() == 2):
		robot.left(50,0.5)	#Turn left 90 degrees
	if (getDirection() == 3):
		robot.left(50,1.0)	#Turn left 180 degrees	
	robot.forward(50, 1.0)
	setDirection(1)

def down():
	if (getDirection() == 0):
		robot.right(50,1.0)	#Turn right 180 degrees
	if (getDirection() == 1):
		robot.right(50,0.5)	#Turn right 90 degrees
	if (getDirection() == 3):
		robot.left(50,0.5)	#Turn left 90 degrees
	robot.forward(50, 1.0)
	setDirection(2)

def left():
	if (getDirection() == 0):
		robot.left(50,0.5)	#Turn left 90 degrees
	if (getDirection() == 1):
		robot.right(50,1.0)	#Turn right 180 degrees
	if (getDirection() == 2):
		robot.right(50,0.5)	#Turn right 90 degrees
	robot.forward(50, 1.0)
	setDirection(3)

def setDirection(direction):
	global di
	di = direction

def getDirection():
	global di
	return di

path = 'ddldll'
di = 0 		#direction: 0 = up, 1 = right, 2 = down, 3 = left
SolvePath(path, di)
	
