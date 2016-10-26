import numpy as np
import cv2 as cv
from scipy.misc import imread,imsave,imresize
import copy

#sources:
#http://www.pyimagesearch.com/2015/04/06/zero-parameter-automatic-canny-edge-detection-with-python-and-opencv/ 
def applyFilter(dimensions,filter_string, img_array,coeff):
    filter_grid=[]
    new_img_array=copy.deepcopy(img_array)
    if (dimensions[0]*dimensions[1])==len(filter_string):   
       #print(len(img_array)) 
       for x in range(0,dimensions[0]):
           row=[]
           for y in range(0,dimensions[1]):
               row.append(int(filter_string[x*dimensions[0]+y]))   
           filter_grid.append(row)
       #print(filter_grid)
      # print(img_array[0])
      # print(img_array[1])
      # print(img_array[2])
      # print(img_array[3])              
       for i in range(0,len(img_array)):
          for j in range(0,len(img_array[0])):
              sum_pixel=0
              for x in range(-1,2):
                  for y in range(-1,2): 
                     # print(i+x)
                     # print(j+y)
                      if i+y<len(img_array) and j+x<len(img_array[0]):
                         sum_pixel+=img_array[i+y][j+x]*filter_grid[y+1][x+1]
              #        print(sum_pixel)
#*filter_grid[x+1][y+1]                
              #print(sum_pixel)
                #  print('x')
              new_img_array[i][j]=sum_pixel*coeff            
      # print(img_array)   
      # print(new_img_array)     
              #sum_pixel+=img_array[i][j]*filter_grid[1][1]
              
       return new_img_array       
    else:
        return 'error'

def main():

    img=imread('picture.jpg')
    difference=.25
    img_median= np.median(img)
    min_level=max(0,(1-difference)*img_median)
    max_level=min(255,(1+difference)*img_median)
    img_canny=cv.Canny(img,min_level,max_level)
    
    filter_string='010111010'
    x=3
    y=3
    img_array=[[0,1,1,0],[0,1,1,0],[0,0,0,0],[0,0,0,0]] 
    img_arr=np.asarray(img_canny,dtype="int32")
    for i in range(0,len(img_arr)):
        for j in range(0,len(img_arr[0])):
            if img_arr[i][j]==255:
                img_arr[i][j]=1
    print(img_arr)
    coeff=.2
    val = applyFilter([x,y],filter_string, img_arr,coeff)
    if type(val)==str:
        return -1
    print(val) 
   # cv.imwrite('x.jpg',val)
   # img_x=cv.imread('x.jpg')
    for i in range(0,len(val)):
        for j in range(0,len(val[0])):
            if val[i][j]==1:
                val[i][j]=255
    cv.imwrite('x.jpg',val)
    img_x=cv.imread('x.jpg') 
    cv.imshow('x',img_x)
   # cv.imshow('picture',img)
   # cv.imshow('canny',img_canny)
    cv.waitKey(0)
    
    


main()
