def trans_main():
	#this script will convert a black and white image into a character array
	global rad
	import numpy
	from scipy.misc import imread,imsave,imresize
	from ops import avg,car_points,car_dim
	import copy
	BLACK= '[0 0 0]'
	WHITE='255 255 255'
	img= imread('extracted.jpg')
	jake = len(img)
	marley = len(img[0])
	img_resized=imresize(img,(jake,marley))
	arr=numpy.asarray(img_resized,dtype="int32")
	output=''
	oh = []
	for i in range(0,len(arr)):
		tmp = ''
		for j in range(0,len(arr[0])):
			if arr[i][j][0]>150 and arr[i][j][0]>arr[i][j][1] and arr[i][j][0]>arr[i][j][2]:
				output=output+'1'
				tmp=tmp+'1'
			elif arr[i][j][1]>150 and arr[i][j][1]>arr[i][j][0] and arr[i][j][1]>arr[i][j][2]:
				output=output+'2'
				tmp=tmp+'2'
			elif arr[i][j][2]>150 and arr[i][j][2]>arr[i][j][0] and arr[i][j][2]>arr[i][j][1]:
				output=output+'3'
				tmp=tmp+'3'
			else: 
				output=output+'0'
				tmp=tmp+'0'
		output=output+'\n'	
		oh.append(tmp)
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
	radis = float(max(abs(pt3[len(pt3)-1][0]-pt3[0][0]),abs(pt3[len(pt3)-1][1]-pt3[0][1]))+1)/(.9)
	radis = int(radis)
	radis1 = max(abs(pt2[len(pt2)-1][0]-pt2[0][0]),abs(pt2[len(pt2)-1][1]-pt2[0][1]))+1
	no=[]
	ones = 0
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
	for i in range(len(no)):
		for j in range(len(no[i])-1):
			if (i==0):
				nono[i][j]=1
			elif(j == 0):
				nono[i][j]=1
			elif (i==len(no)-1):
				nono[i][j]=1
			elif (j==(len(no[i])-2)):
				nono[i][j+1]=1
			elif no[i][j]==1:
				uns+=1
				for x in range(radis):
					for y in range(radis):
						if (i+x-(radis/2))>0 and (i+x-(radis/2))<len(no) and (j+y-(radis/2))>0 and (j+y-(radis/2))<len(no[i]):
							if nono[i+x-(radis/2)][j+y-(radis/2)]==0:
								nono[i+x-(radis/2)][j+y-(radis/2)]=1


	die = (pt3[len(pt3)-1][0]-pt3[0][0],pt3[len(pt3)-1][1]-pt3[0][1])
	rad=die
	f = open('maze.txt', 'w')
	f.seek(0)
	for ele in nono:
		tmp=''
		for ele1 in ele:
			tmp+=str(ele1)
		f.write(str(tmp))
		f.write('\n')
	f.close();
	return die

def printee(what):
	print('\n')
	for ele in what:
		print(ele)
