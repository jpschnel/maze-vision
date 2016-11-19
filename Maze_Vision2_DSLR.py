#1 camera takes picture
#2. edge detection
#3. recognize object
#4.translate image
#5.shortest path
import os
import cv2 as cv

pi_camera='192.168.0.12'
pi_car='192.168.1.45'
def maze_vision():
##################################################################
#Camera Module
#Connects to pi 
#Captures picture from connected camera
#copies to a local destination
#
######################################################
    os.system('ssh '+pi_camera)
    os.system('gphoto2 --capture-image-and-download --force-overwrite')
    img = cv.imread('capt_0000.jpg')
    imsave('Picture.jpg',img)
    del img

################################################################
#Image processing
#calls outside python script to analyse for objects
#returns color coded jpg 'extracted.jpg'
#
#############################################################
    os.system('python Edge_Detection.py')
    os.system('python recognize_object.py')

####################################################
#Image_conversion
#converts Image to number array
#0 represents boundaries where you can't travel,1 is free space
#2 shows cars position(originally blue), 3 is the end goal(originally red)
###################################################

    
    os.system('python img_translator.py')


    
    os.system('cd Florence')
    os.system('python Solve_Path.py')
    os.system('cd ..')











maze_vision()
