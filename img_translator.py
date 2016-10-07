#this script will convert a black and white image into a character array
#import image
import numpy
from scipy.misc import imread,imsave,imresize
#predefined values
BLACK= '[0 0 0]'
WHITE='255 255 255'
img= imread('extracted.jpg')
img_resized=imresize(img,(32,64))
arr=numpy.asarray(img_resized,dtype="int32")


#print (len(arr))
#print(arr)
#print(arr[20][20])
#print(arr)
#print(arr[0][0].tostring)
output=''
for i in range(0,len(arr)):
	for j in range(0,len(arr[0])):
		
		if arr[i][j][0]==255 and arr[i][j][1]==255 and arr[i][j][2]==255:
			#arr[i][j]=1
			output=output+'1'
		elif arr[i][j][0]==0 and arr[i][j][1]==0 and arr[i][j][2]==0:
			#arr[i][j]=0
			output=output+'0'
		elif arr[i][j][0]==255 and arr[i][j][1]==0 and arr[i][j][2]==0:
			#arr[i][j]=2
			output=output+'2'
		elif arr[i][j][0]==0 and arr[i][j][1]==0 and arr[i][j][2]==0:
			#arr[i][j]=3
			output=output+'3'
		else: 
			output=output+'1'

	output=output+'\n'	
		#print(arr[i][j])
		#print(arr[i][j].tostring)
			#print('white');
			#arr[i][j]=0
#print(arr[220][201])
print(output)
#imsave('img_new.jpg',img)
