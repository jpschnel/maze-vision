# 0 = open space, 1=boundary , 2= the robot, 3= finish

def maze_vision():
	path= ''
	maze=[]
	maze.append(list('000000000000000000002'))
	maze.append(list('000000000000000000000'))
	maze.append(list('000000000000000000000'))
	maze.append(list('000000000000001000000'))
	maze.append(list('000300000000111100000'))
	#print(maze)
	fx=0
	fy=0
	sx=0
	sy=0
	#print(maze[0][8])
	#print(len(maze[0]))
	for x in range(0,len(maze[0])):
		for y in range(0,len(maze)):
			if maze[y][x]=='2':
				sx=x
				sy=y 
			elif maze[y][x]=='3':
				fx=x
				fy=y
	edges4 = get_edges4(maze)
	edges8 = get_edges8(maze)
	edges = plot_edges(edges8,edges4)
	ng = edges[1]
	edges = edges[0]
	ng.insert(0,(sy,sx))
	ng.append((fy,fx))
	print(ng)
	print('\n')
	printee(edges)
	print('\n')
	#printee(for_rep(maze))
	edge_maze=merge_em(maze,edges)
	#print('\n')
	printee(edge_maze)
	wata = False
	#if findd(ng[0][1],ng[0][0],ng[1][0],edge_maze):
	#	if findl(ng[1][0],ng[0][1],ng[1][1],edge_maze):
	#		print("fooka")
	graph = get_nodes(ng,edge_maze,[])
	printee(graph)
	print("sx="+str(sx))
	print("sy="+str(sy))
	print("fx="+str(fx))
	print("fy="+str(fy))
	#ans= distance(maze,sx,sy,fx,fy)
	#print ("the shortest path is "+ans+ " spaces")
	print(path)
	
def get_nodes(ng,edge_maze,explored):
	i = 0
	j = 0
	nodes = []
	for i in range(0,len(ng)):
		connected0 = True
		connected1 = True
		direction = 'v'
		#print("Doing:"+str(i)+" now.")
		for j in range(i+1,len(ng)):
			#print("Doing:"+str(j)+" now.")
			if ((ng[i][0]<ng[j][0] and not findd(ng[i][1],ng[i][0],ng[j][0],edge_maze)) or (ng[i][1]>ng[j][1] and not findl(ng[j][0],ng[i][1],ng[j][1],edge_maze)) or (ng[i][0]>ng[j][0] and not findu(ng[i][1],ng[i][0],ng[j][0],edge_maze)) or (ng[i][1]<ng[j][1] and not findr(ng[j][0],ng[i][1],ng[j][1],edge_maze))):
				connected0 = False
				direction = 'h'
			if ((ng[i][0]<ng[j][0] and not findd(ng[j][1],ng[i][0],ng[j][0],edge_maze)) or (ng[i][1]>ng[j][1] and not findl(ng[i][0],ng[i][1],ng[j][1],edge_maze)) or (ng[i][0]>ng[j][0] and not findu(ng[j][1],ng[i][0],ng[j][0],edge_maze)) or (ng[i][1]<ng[j][1] and not findr(ng[i][0],ng[i][1],ng[j][1],edge_maze))):
				connected1= False
			if connected0 == True or connected1 == True :
				dis = abs(ng[i][0]-ng[j][0])+abs(ng[i][1]-ng[j][1])
				#print("fooka "+str((i,j,dis,direction)))
				nodes.append((i,j,dis,direction))
	#if findd(ng[0][1],ng[0][0],ng[1][0],edge_maze):
#		if findl(ng[1][0],ng[0][1],ng[1][1],edge_maze):
#			dis = abs(ng[0][0]-ng[1][0])+abs(ng[0][1]-ng[1][1])
#			print("fooka"+str(dis))
	print("UD")
	return nodes

def generator(nodes,i,j,direction):
	print("UD")

	
def findu(x,s,d,maze):
	while s!=d:
		s=s-1
		#print(s)
		if s== -1:
			return False
		if maze[s][x]==' 1':
			return False
	return True
	
def findd(x,s,d,maze):
	while s!=d:
		s=s+1
		#print(s)
		if s== len(maze):
			return False
		if maze[s][x]==' 1':
			return False
	return True
	
def findl(y,s,d,maze):
	while s!=d:
		s=s-1
		#print(s)
		if s== -1:
			return False
		if maze[y][s]==' 1':
			return False
	return True
	
def findr(y,s,d,maze):
	while s!=d:
		s=s+1
		#print(s)
		if s == len(maze):
			return False
		if maze[y][s]==' 1' :
			return False
	return True

def merge_em(maze,edges):
	final = []
	maze = for_rep(maze)
	for x in range(0,len(maze)):
		finaly = []
		for y in range(0,len(maze[0])):
			if edges[x][y]=='EE':
				finaly.append('EE')
			else:
				finaly.append(maze[x][y])
		final.append(finaly)
	return final
	
def plot_edges(edges,edges2):
	#printee(edges)
	edges = fatter(edges,'-0')
	edges2 = fatter(edges2,'-0')
	final=[]
	nodachi = []
	for y in range(1,len(edges)-1):
		final1=[]
		for x in range(1,len(edges[0])-1):
			if edges[y][x]=='-7':
				if '-' not in edges[y-1][x-1] and '-' not in edges[y][x-1] and '-' not in edges[y-1][x]:
					edges[y-1][x-1]='EE'
					nodachi.append((y-2,x-2))
				if '-' not in edges[y+1][x-1] and '-' not in edges[y][x-1] and '-' not in edges[y+1][x]:
					edges[y+1][x-1]='EE'
					nodachi.append((y,x-2))
				if '-' not in edges[y-1][x+1] and '-' not in edges[y][x+1] and '-' not in edges[y-1][x]:
					edges[y-1][x+1]='EE'
					nodachi.append((y-2,x))
				if '-' not in edges[y+1][x+1] and '-' not in edges[y][x+1] and '-' not in edges[y+1][x]:
					edges[y+1][x+1]='EE'
					nodachi.append((y,x))
			if edges[y][x] in ['-4','-5','-6'] and edges2[y][x] in ['-2','-3']:
				if '-' not in edges[y-1][x-1] and '-' not in edges[y][x-1] and '-' not in edges[y-1][x]:
					edges[y-1][x-1]='EE'
					nodachi.append((y-2,x-2))
				if '-' not in edges[y+1][x-1] and '-' not in edges[y][x-1] and '-' not in edges[y+1][x]:
					edges[y+1][x-1]='EE'
					nodachi.append((y,x-2))
				if '-' not in edges[y-1][x+1] and '-' not in edges[y][x+1] and '-' not in edges[y-1][x]:
					edges[y-1][x+1]='EE'
					nodachi.append((y-2,x))
				if '-' not in edges[y+1][x+1] and '-' not in edges[y][x+1] and '-' not in edges[y+1][x]:
					edges[y+1][x+1]='EE'
					nodachi.append((y,x))
	#print('\n\n')
	print(nodachi)
	return skimp(edges),nodachi
	
def add_node(nx,ny):
	d = edge_node
	d.x=nx
	d.y=ny
	return d
	
def print_node(nodes):
	for ele in nodes:
		print(ele.x,ele.y)
	
def get_edges4(maze):
	finaly = fatter(maze,'1')
	final = []
	for y in range(1,len(maze)+1):
		final1=[]
		for x in range(1,len(maze[0])+1):
			o = 0
			if finaly[y][x]=='1':
				o-=4
			if finaly[y+0][x-1]=='1':
				o+=1
			if finaly[y-1][x+0]=='1':
				o+=1
			if finaly[y+1][x+0]=='1':
				o+=1
			if finaly[y+0][x+1]=='1':
				o+=1
			p=o
			o=str(o)
			if p>-1:
				o=' '+o
			final1.append(o)
		final.append(final1)
	return final
	
def get_edges8(maze):
	finaly = fatter(maze,'1')
	final = []
	for y in range(1,len(maze)+1):
		final1=[]
		for x in range(1,len(maze[0])+1):
			o = 0
			if finaly[y][x]=='1':
				o-=8
			if finaly[y+0][x-1]=='1':
				o+=1
			if finaly[y-1][x-1]=='1':
				o+=1
			if finaly[y+1][x-1]=='1':
				o+=1
			if finaly[y-1][x+0]=='1':
				o+=1
			if finaly[y+1][x+0]=='1':
				o+=1
			if finaly[y+0][x+1]=='1':
				o+=1
			if finaly[y-1][x+1]=='1':
				o+=1
			if finaly[y+1][x+1]=='1':
				o+=1
			p=o
			o=str(o)
			if p>-1:
				o=' '+o
			final1.append(o)
		final.append(final1)
	return final
	
def fatter(list,hold):
	finaly = [[hold]*(len(list[0])+2)]
	for ele in list:
		toap = []
		f = [hold]
		for item in ele:
			f.append(item)
		f.append(hold)
		finaly.append(f)
	finaly.append(finaly[0])
	return finaly
	
def skimp(list):
	final =[]
	for x in range(1,len(list)-1):
		finaly = []
		for y in range(1,len(list[0])-1):
			finaly.append(list[x][y])
		final.append(finaly)
	return final
	
def for_rep(maze):
	final =[]
	for x in range(0,len(maze)):
		finaly = []
		for y in range(0,len(maze[0])):
			finaly.append(' '+maze[x][y])
		final.append(finaly)
	return final
	
def printee(what):
	for ele in what:
		print(ele)
	
def distance(maze, sx, sy, fx, fy):

	if sx==fx and sy==fy:
		return ''	
	
	maze[sy][sx] = '4'
	longstring='w'*2000
	right = longstring
	down = longstring
	left = longstring
	up = longstring

	if sx+1 < len(maze[0]):
		if (maze[sy][sx+1]=='0' and not maze[sy][sx+1]=='4') or maze[sy][sx+1]=='3':
			right = 'r'+distance(maze, sx+1, sy, fx, fy)
	if sy+1 < len(maze):
		if (maze[sy+1][sx]=='0' and not maze[sy+1][sx]=='4') or maze[sy+1][sx]=='3':
			down = 'd'+distance(maze, sx, sy+1, fx, fy)
	if sx-1 >= 0:
		if (maze[sy][sx-1]=='0' and not maze[sy][sx-1]=='4') or maze[sy][sx-1]=='3':
			left = 'l'+distance(maze, sx-1, sy, fx, fy)
	if sy-1 >= 0:
		if (maze[sy-1][sx]=='0' and not maze[sy-1][sx]=='4') or maze[sy-1][sx]=='3':
			up =  'u'+distance(maze, sx, sy-1, fx, fy)

	maze[sy][sx] = '0'
    
	
	min_dir=min(len(right), len(down), len(left), len(up))
	if len(right)==min_dir:
		return right
	elif len(left)==min_dir:
		return left
	elif len(up)==min_dir:
		return up
	else:
		return down

#	up= int(sy-1)
#	down= int(sy+1)
#	left = int(sx-1)
#	right = int(sx+1) 
#	print(str(sx)+','+str(sy))
	
#	updist=3333333
#	downdist=6666666
#	leftdist=5555555
#	rightdist=4444444
#	if maze[sy][sx]=='3':						#reached finish			
#		print(hit)
#		return 0								#return
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
	
#	print(down)
#	if down < (len(maze)-1):
#		print('w')
#		print(maze[down][sx])
		

#		if maze[down][sx]=='0':
#			maze[sy][sx]='4'
			#path path +'d'
#			downdist= 1 + distance(maze,down,sy,fx,fy,path)
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

#	return min(updist,downdist,rightdist,leftdist)
#	sum2= min(rightdist,leftdist)
#	return min(sum2,sum1)

class edge_node:
	x=0
	y=0
		
maze_vision()
