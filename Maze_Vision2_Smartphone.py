#1 camera takes picture
#2. edge detection
#3. recognize object
#4.translate image
#5.shortest path
import os


def maze_vision():
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

    
   # os.system('python img_translator.py')
    os.system('python Amazeing.py > path.txt')

    
#    os.system('cd Florence')
#    os.system('python Solve_Path.py')
#    os.system('cd ..')











maze_vision()
