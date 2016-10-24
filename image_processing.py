import numpy as np
import cv2 as cv
from scipy.misc import imread,imsave,imresize


#sources:
#http://www.pyimagesearch.com/2015/04/06/zero-parameter-automatic-canny-edge-detection-with-python-and-opencv/ 
def main():

    img=imread('picture.jpg')
    difference=.25
    img_median= np.median(img)
    min_level=max(0,(1-difference)*img_median)
    max_level=min(255,(1+difference)*img_median)
    img_canny=cv.Canny(img,min_level,max_level)
 
    cv.imshow('picture',img)
    cv.imshow('canny',img_canny)
    cv.waitKey(0)
    



main()
