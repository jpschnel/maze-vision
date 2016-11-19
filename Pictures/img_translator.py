def trans_main():
	#this script will convert a black and white image into a character array
	#import image
	import numpy
	from scipy.misc import imread,imsave,imresize
	from ops import avg,car_points,car_dim
	import copy
	#predefined values
	BLACK= '[0 0 0]'
	WHITE='255 255 255'
	img= imread('extracted.jpg')
	jake = len(img)
	marley = len(img[0])
	#print(jake,marley)
	img_resized=imresize(img,(jake,marley))
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
	#print(output)
	pt3 = car_points(oh,'3')
	pt2 = car_points(oh,'1')
	av3 = avg(pt3);
	av1 =  avg(pt2);
	find = car_dim(pt3)
	dim = (find[0][1]-find[0][0])+1,(find[1][1]-find[1][0])+1
	floor_dim = (marley/dim[0])*4.3,(jake/dim[1])*3.9
	pixel_value = floor_dim[0]/marley,floor_dim[1]/jake
	car_val = av3[0]*pixel_value[0],av3[1]*pixel_value[1]
	target_val = av1[0]*pixel_value[0],av1[1]*pixel_value[1]
	radis = (max(abs(pt3[len(pt3)-1][0]-pt3[0][0]),abs(pt3[len(pt3)-1][1]-pt3[0][1]))+1)/2
	radis1 = max(abs(pt2[len(pt2)-1][0]-pt2[0][0]),abs(pt2[len(pt2)-1][1]-pt2[0][1]))+1
	#justins code starts here
	#gaaaaaaaaah
	#xcord= av3[1]
	#ycord= av3[0]
	#for dist in 
	no=[]
	ones = 0
	#radis = 3
	for i in range(len(oh)):
		temp=[]
		for j in range(len(oh[i])):
			if oh[i][j]=='1' or oh[i][j]=='3':
				if i==av3[1] and j==av3[0]:
					temp.append(2)
				elif i==av1[1] and j==av1[0]:
					temp.append(3)
				else:
					temp.append(0)
			elif oh[i][j]=='2':
				temp.append(1)
				ones+=1
			else:
				temp.append(0)
		no.append(temp[:])
	nono=copy.deepcopy(no)
	uns=0
	#print(len(no),len(no[i]))
	for i in range(len(no)):
		#print(i)
		for j in range(len(no[i])-1):
			#print(j)
			if no[i][j]==1:
				uns+=1
				#print(uns/ones)
				for x in range(radis):
					for y in range(radis):
						#print((i-x-radis),(j-y-radis))
						if (i+x-(radis/2))>0 and (i+x-(radis/2))<len(no) and (j+y-(radis/2))>0 and (j+y-(radis/2))<len(no[i]):
							if nono[i+x-(radis/2)][j+y-(radis/2)]==0:
								nono[i+x-(radis/2)][j+y-(radis/2)]=1

	#printee(nono)
	#print(abs(max(pt3[0])-min(pt2[0])))
	#print(abs(max(pt3[1])-min(pt2[1])))
	#print(pt3[0],pt3[len(pt3)-1])
#	print(radis)
#	print(radis1)
#	print("The size of each pixel is "+str(pixel_value))
#	print("The Car's Center is: ("+str(av3[1])+","+str(av3[0])+") or at ("+str(car_val[1])+'",'+str(car_val[0])+'").')
#	print("The Target's Center is: ("+str(av1[1])+","+str(av1[0])+") or at ("+str(target_val[1])+'",'+str(target_val[0])+'").')
#	print("The floor size is "+str(floor_dim[1])+'" by '+str(floor_dim[0])+'".')
	f = open('maze.txt', 'w')
	f.seek(0)
	for ele in nono:
		tmp=''
		for ele1 in ele:
			tmp+=str(ele1)
		f.write(str(tmp))
		f.write('\n')
	f.close();
#	print(len(no),len(no[i]))
	#x is going from left to right, and y is up and down
	#imsave('img_new.jpg',img)

def printee(what):
	print('\n')
	for ele in what:
		print(ele)
