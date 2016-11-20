def avg(ptx):
	ex=0
	ey=0
	for cord in ptx:
		ey=ey+cord[0]
		ex=ex+cord[1]
	ex=ex/len(ptx)
	ey=ey/len(ptx)
	return ex,ey

# Takes in a floor map and a target index, then gives the points which it exists
def car_points(floor_map,target):
	pt3 = []
	iy=0
	for y in floor_map:
		ix=0
		for x in y:
			if x==target:
				pt3.append([iy,ix])
			ix+=1
		iy+=1
	return pt3

def car_dim(pt3):
	xs=[90,0]
	ys=[120,0]
	for ele in pt3:
		if ele[0]<xs[0]:
			xs[0]=ele[0]
		if ele[0]>xs[1]:
			xs[1]=ele[0]
		if ele[1]<ys[0]:
			ys[0]=ele[1]
		if ele[1]>ys[1]:
			ys[1]=ele[1]
	return(xs,ys)

def printee(what):
	print('\n')
	for ele in what:
		print(ele)
