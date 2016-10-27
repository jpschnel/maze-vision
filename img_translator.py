#this script will convert a black and white image into a character array
#import image
import numpy
from scipy.misc import imread,imsave,imresize
from ops import avg,car_points,car_dim
#predefined values
BLACK= '[0 0 0]'
WHITE='255 255 255'
img= imread('extracted.jpg')
img_resized=imresize(img,(90,120))
arr=numpy.asarray(img_resized,dtype="int32")

#print (len(arr))
#print(arr)
#print(arr[20][20])
#print(arr)
#print(arr[0][0].tostring)
output=''
oh = []
for i in range(0,len(arr)):
	tmp = ''
	for j in range(0,len(arr[0])):
		if arr[i][j][0]>150 and arr[i][j][0]>arr[i][j][1] and arr[i][j][0]>arr[i][j][2]:
			#arr[i][j]=1
			output=output+'1'
			tmp=tmp+'1'
		elif arr[i][j][1]>150 and arr[i][j][1]>arr[i][j][0] and arr[i][j][1]>arr[i][j][2]:
			#arr[i][j]=2
			output=output+'2'
			tmp=tmp+'2'
		elif arr[i][j][2]>150 and arr[i][j][2]>arr[i][j][0] and arr[i][j][2]>arr[i][j][1]:
			#arr[i][j]=3
			output=output+'3'
			tmp=tmp+'3'
		else: 
			output=output+'0'
			tmp=tmp+'0'
	output=output+'\n'	
	oh.append(tmp)
		#print(arr[i][j])
		#print(arr[i][j].tostring)
			#print('white');
			#arr[i][j]=0
#print(arr[220][201])
print(output)
pt3 = car_points(oh,'3')
pt2 = car_points(oh,'1')
av3 = avg(pt3);
av1 =  avg(pt2);
find = car_dim(pt3)
dim = (find[0][1]-find[0][0])+1,(find[1][1]-find[1][0])+1
floor_dim = (120/dim[0])*4.3,(90/dim[1])*3.9
pixel_value = floor_dim[0]/120,floor_dim[1]/90
car_val = av3[0]*pixel_value[0],av3[1]*pixel_value[1]
target_val = av1[0]*pixel_value[0],av1[1]*pixel_value[1]
print("The size of each pixel is "+str(pixel_value))
print("The Car's Center is: ("+str(av3[1])+","+str(av3[0])+") or at ("+str(car_val[1])+'",'+str(car_val[0])+'").')
print("The Target's Center is: ("+str(av1[1])+","+str(av1[0])+") or at ("+str(target_val[1])+'",'+str(target_val[0])+'").')
print("The floor size is "+str(floor_dim[1])+'" by '+str(floor_dim[0])+'".')
#x is going from left to right, and y is up and down
#imsave('img_new.jpg',img)
