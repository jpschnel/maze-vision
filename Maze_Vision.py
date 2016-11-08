#import subprocess 
import os
import string
import numpy
from scipy.misc import imread,imsave
import Solve_path
def maze_vision():
	pi_car= '192.168.0.12'
	pi_camera='192.168.1.145'

	#os.system("echo this")
##################################################################
#Camera Module
#Connects to pi 
#Captures picture from connected camera
#copies to a local destination
#
######################################################
	#os.system('ssh '+pi_camera) #ssh into camera connected pi


	os.system('gphoto2 --capture-image-and-download --force-overwrite')
	img = imread('capt_0000.jpg')

	#os.system('quit')
	imsave('source-images/original.jpg',img)
	del img    #clear image out of memory

################################################################
#Image processing
#calls outside python script to analyse for objects
#returns color coded jpg 'extracted.jpg'
#
#############################################################

        os.system('python image_processing.py')
	



####################################################
#Image_conversion
#converts Image to number array
#0 represents boundaries where you can't travel,1 is free space
#2 shows cars position(originally blue), 3 is the end goal(originally red)
###################################################

	os.system('python img_translator.py>tmp.txt') #outside script to convert it all
	f = open(i,'r')
	
	img_converted = []
	i=0
	for line in f.readlines():
		line.replace('\n','')
		img_converted[i] = line
		i=i+1
	
#####################################################
#Shortest path module
#calculates the shortest path and returns a set of directions 
#for the vehicle to go in
#
######################################################

    ops.system("python maze_vision_algo.py")




	
##################################################
#Maze traversal
#ssh into car pi
#send directions and deploy
####################################################
     os.system("python Solve_Path.py")	
     os.system('ssh '+ pi_car)
	








maze_vision()
