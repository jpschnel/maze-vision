# 0 = open space, 1=boundary , 2= the robot, 3= finish

def maze_vision():
	path= ''

	maze=[]

	maze.append(list('000000002000000'))
	maze.append(list('000000003001100'))
	maze.append(list('000000000000000'))
	maze.append(list('000000000000000'))
	maze.append(list('000000000000000'))
	maze.append(list('000000000000000'))
	#print(maze)
	fx=0
	fy=0
	sx=0
	sy=0
	#print(maze[0][8])
	#print(len(maze[0]))
	for x in range(0,len(maze[0])-1):
		for y in range(0,len(maze)-1):
			if maze[y][x]=='2':
				sx=x
				sy=y 
			elif maze[y][x]=='3':
				fx=x
				fy=y
			
	#print(fx)
	#print(fy)
	#print(sx)
	#print(sy)
	ans= distance(maze,sx,sy,fx,fy,path)
	print ("the shortest path is "+str(ans)+ " spaces")
	print(path)


	

	
def distance(maze, sx, sy, fx, fy,path):

	up= int(sy-1)
	down= int(sy+1)
	left = int(sx-1)
	right = int(sx+1) 
	print(str(sx)+','+str(sy))
	
	updist=3333333
	downdist=6666666
	leftdist=5555555
	rightdist=4444444
	if maze[sy][sx]=='3':						#reached finish			
		print(hit)
		return 0								#return
#up		
	
#	if up >-1:
#		if maze[sy][up]=='0':							#if this direction is open
#			maze[sy][up]='4'							#mark it as traveled to
#			path= path +'u'							#add that direction to final path
#			updist= 1+ distance(maze,up,sy,fx,fy,path)	#calculate shortest dist from there
		#if it makes it past here, that was not the shortest distance
			#path= path[:-1]							#remove that direction from final path
			#maze[sy][up]=0							#mark that direction as not traveled
		
#down
	
	print(down)
	if down < (len(maze)-1):
		print('w')
		print(maze[down][sx])
		

		if maze[down][sx]=='0':
			maze[sy][sx]='4'
			#path path +'d'
			downdist= 1 + distance(maze,down,sy,fx,fy,path)
			#path= path[:-1]
			#maze[sy][down]='0'
		#else:
			#downdist=999999
#left 
#	if left>-1:
#		if maze[left][sx]=='0':
#			maze[left][sx]='4'
#			path= path +'l'
#			leftdist= 1+distance(maze,sx,left,fx,fy,path)
#			path= path[:-1]
#			maze[left][sx]='0'
	
#right
#	if right<(len(maze[0])-1):
#		if maze[sx][right]=='0':
#			maze[sx][right]='4'
#			path=path+'r'
#			rightdist= 1+distance(maze,sx,right,fx,fy,path)
#			path=path[:-1]
#			maze[right][sx]='0'
	#print(str(sx)+','+str(sy))	

	return min(updist,downdist,rightdist,leftdist)
#	sum2= min(rightdist,leftdist)
#	return min(sum2,sum1)
	
		
maze_vision()
