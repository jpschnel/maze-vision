#1 camera takes picture
#2. edge detection
#3. recognize object
#4.translate image
#5.shortest path
import os


def maze_vision():
    os.system('python Edge_Detection.py')
    os.system('python recognize_object.py')
    os.system('python img_translator.py')
    os.system('cd Florence')
    os.system('python Solve_Path.py')
    os.system('cd ..')











maze_vision()
