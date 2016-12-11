#Usage
#"python Solve_Path.py path"
#where path is a string of characters (u,r,d,l)

import time
import Robot
import sys

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
		Florence.left(s90,t90)	#Turn left 90 degrees
	if (getDirection() == 2):
		Florence.right(s180,t180)	#Turn right 180 degrees	
	if (getDirection() == 3):
		Florence.right(s90,t90)	#Turn right 90 degrees
	Florence.forward(s, t)
	setDirection(0)


def right():
	if (getDirection() == 0):
		Florence.right(s90,t90)	#Turn right 90 degrees
	if (getDirection() == 2):
		Florence.left(s90,t90)	#Turn left 90 degrees
	if (getDirection() == 3):
		Florence.left(s180,t180)	#Turn left 180 degrees	
	Florence.forward(s, t)
	setDirection(1)

def down():
	if (getDirection() == 0):
		Florence.right(s180,t180)	#Turn right 180 degrees
	if (getDirection() == 1):
		Florence.right(s90,t90)	#Turn right 90 degrees
	if (getDirection() == 3):
		Florence.left(s90,t90)	#Turn left 90 degrees
	Florence.forward(s, t)
	setDirection(2)

def left():
	if (getDirection() == 0):
		Florence.left(s90,t90)	#Turn left 90 degrees
	if (getDirection() == 1):
		Florence.right(s180,t180)	#Turn right 180 degrees
	if (getDirection() == 2):
		Florence.right(s90,t90)	#Turn right 90 degrees
	Florence.forward(s, t)
	setDirection(3)

def setDirection(direction):
	global di
	di = direction

def getDirection():
	global di
	return di



LEFT_TRIM = 0
RIGHT_TRIM = 0

Florence = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)
path = str(sys.argv[1])
di = 2		#direction: 0 = up, 1 = right, 2 = down, 3 = left; direction is always initially set to down
#straight line variables (t,s)
t = 0.55	#time: seconds that the motors are running
s = 50		#speed: controls speed (going straight), can be value 0-255
#90 degree turn variables (t90,s90)
t90 = 0.469 #hehehehehehe
s90 = 50
#180 degree turn variables (t180,s180)
t180 = 0.95
s180 = 50
SolvePath(path, di)
