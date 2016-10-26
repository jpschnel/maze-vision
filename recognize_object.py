import numpy as np
import cv2 as cv
from scipy.misc import imread,imsave,imresize
import copy

def main():

    Source_img= imread('picture.jpg')
    Template_img=imread('robot_template.jpg')
   
    #cv.imshow('source',Source_img)
    #cv.imshow('template',Template_img)
    #cv.waitKey(0)
    #results=[]
    #check starting at 0,0
    #cannot go past bounds so must subtract template size from the original img
    result_columns= len(Source_img)-len(Template_img)+1
    result_rows=len(Source_img[0])-len(Template_img[0])+1
    
    method=eval('cv.TM_CCOEFF')
    
    np.zeros((result_columns,result_rows),dtype=int)
    res=cv.matchTemplate(Source_img,Template_img,method)
    min_val,max_val,min_loc,max_loc=cv.minMaxLoc(res)

    top_left=max_loc
    bottom_right=top_left[0]+len(Template_img),top_left[1]+len(Template_img[0])
    cv.rectangle(Source_img,top_left,bottom_right,255,2)
    cv.imshow('img',Source_img)
    cv.waitKey(0)
    #print(result_columns)
    #print(result_rows)
    #cv.matchTemplate(img
    
    
    #results.append(result)

main()
