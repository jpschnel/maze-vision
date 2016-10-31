import numpy as np
import cv2 as cv
from scipy.misc import imread,imsave,imresize
import copy



def main():
    Source_img= imread('picture.jpg')
    new_img=copy.deepcopy(Source_img)
    Robot_img=imread('robot_template.jpg')
    End_img=imread('end_template.jpg')

    new_img_arr=np.asarray(new_img,dtype="int32")
    for i in range(0,len(new_img_arr)):
        for j in range(0,len(new_img_arr[0])):
            new_img_arr[i][j]=[0,0,0]
    cv.imwrite('tmp.jpg',new_img_arr)
    new_img=imread('tmp.jpg')    
    #cv.imshow('x',End_img)
    #cv.imshow('source',Source_img)
    #cv.imshow('template',Template_img)
    #cv.waitKey(0)
    #results=[]
    #check starting at 0,0
    #cannot go past bounds so must subtract template size from the original img
    result_columns= len(Source_img)-len(Robot_img)+1
    result_rows=len(Source_img[0])-len(Robot_img[0])+1
    
    method=eval('cv.TM_CCOEFF')
    
    np.zeros((result_columns,result_rows),dtype=int)
    res=cv.matchTemplate(Source_img,Robot_img,method)
    min_val_bot,max_val_bot,min_loc_bot,max_loc_bot=cv.minMaxLoc(res)

    top_left_bot=max_loc_bot
    bottom_right_bot=top_left_bot[0]+len(Robot_img[0]),top_left_bot[1]+len(Robot_img)
    
    cv.rectangle(new_img,top_left_bot,bottom_right_bot,[255,0,0],-1)


    res=cv.matchTemplate(Source_img,End_img,method)
    min_val,max_val,min_loc,max_loc=cv.minMaxLoc(res)
    top_left_end=max_loc
    bottom_right_end=top_left_end[0]+len(End_img[0]),top_left_end[1]+len(End_img)

    canny_img=imread('picture_canny.jpg')
    
    cv.rectangle(new_img,top_left_end,bottom_right_end,[0,0,255],-1)
        
    canny_img_array=np.asarray(canny_img,dtype="int32")
    
    #print(canny_img_array)
    for i in range(0,len(canny_img_array)):
        for j in range(0,len(canny_img_array)):
            if canny_img_array[i][j]>120:
                 canny_img_array[i][j]=255
            else:
                 canny_img_array[i][j]=0
    new_img_array=np.asarray(new_img,dtype="int32")
    #print(new_img_array)
    #print('x')
    #print(canny_img_array)
    for i in range(0,len(new_img_array)):
        for j in range(0,len(new_img[0])):
            if new_img_array[i][j][0]==0 and new_img_array[i][j][2]==0:
                if canny_img_array[i][j]==255:
                    new_img_array[i][j][1]=255
                #new_img_array[i][j]=canny_img_array[i][j]
    
    cv.imwrite('tmp.jpg',new_img_array)
    new_img=imread('tmp.jpg')



    cv.imshow('robot_template',imresize(Robot_img,(len(Robot_img)*2,len(Robot_img[0])*2)))
    cv.imshow('end_template',imresize(End_img,(len(End_img)*2,len(End_img[0])*2)))
    cv.imshow('original_img',Source_img)
    cv.imshow('extracted_img',new_img)

    cv.waitKey(0)
    imsave('extracted.jpg',new_img)
    #print(result_columns)
    #print(result_rows)
    #cv.matchTemplate(img
    
   
    #results.append(result)

main()
