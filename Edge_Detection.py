import numpy as np
import cv2 as cv
import copy
from scipy.misc import imread,imsave,imresize
import scipy.ndimage as sp

def genHistogram(img_arr):
    Hist=[]
    for x in range(0,256):
       Hist.append(0)
    for i in range(0,len(img_arr)):
        for j in range(0,len(img_arr[0])):
           #print(img_arr[i][j])            
           Hist[img_arr[i][j]]+=1
    return Hist
def LoG_Filter(img_arr):
    new_img_arr=copy.deepcopy(img_arr)
    LoG_Mask=[[0,0,1,0,0],[0,1,2,1,0],[1,2,-16,2,1],[0,1,2,1,0],[0,0,1,0,0]]
    #print(LoG_Mask)

    i=0
    j=0
    for i in range(0,len(img_arr)):
        for j in range(0,len(img_arr[0])):
            sum_pixel=0
             
            for x in range(0,len(LoG_Mask)):
               for y in range(0,len(LoG_Mask)):
                   if(i+(x-2))>=0 and (j+(y-2))>=0 and (i+(x-2))<len(img_arr) and (j+(y-2))<len(img_arr[0]):
                       sum_pixel+=LoG_Mask[x][y]*(img_arr[i+(x-2)][j+(y-2)])      
            new_img_arr[i][j]=sum_pixel
           # if sum_pixel>=0:
            #    new_img_arr[i][j]=255
            #else: 
             #   new_img_arr[i][j]=0
                   
    return new_img_arr
def main(input_pic):
    img = cv.imread(input_pic,cv.CV_LOAD_IMAGE_GRAYSCALE)
    img=sp.gaussian_filter(img,sigma=3)
    img= imresize(img,((len(img)/10),(len(img[0])/10)))
    img_arr=np.asarray(img,dtype="int32")

    LoG_arr=LoG_Filter(img_arr)
    cv.imwrite('LoG_image.jpg',LoG_arr)
    LoG_arr=cv.imread('LoG_image.jpg',cv.CV_LOAD_IMAGE_GRAYSCALE)
    Hist=genHistogram(LoG_arr)
    #print(Hist)
    for i in range(0,len(LoG_arr)):
        for j in range(0,len(LoG_arr[0])):
             if LoG_arr[i][j]<200:
                 LoG_arr[i][j]=0
             else:
                 LoG_arr[i][j]=255
     
    cv.imwrite('LoG_image.jpg',LoG_arr)    
    #img_new=cv.imread('LoG_image.jpg',cv.CV_LOAD_IMAGE_GRAYSCALE)
    

    

main('mazeinput.jpg')

