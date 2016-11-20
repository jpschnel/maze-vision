
#import time
#from datetime import datetime

def mvsp(die):
	path= ''
	maze=[]
	maze = get_maze()
	#printee(maze)
	fx=0
	fy=0
	sx=0
	sy=0
	#st=strftime("%S", gmtime())
	#st = datetime.now()
	#st = st.microsecond
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
	edge_maze=merge_em(maze,edges)
	#printee(maze)
	wata = False
	graph = get_nodes(ng,edge_maze,[])
	#printee(graph)
	compressed = compress(graph,ng)
	#printee(compressed)
	#print('\n')
	#printee(compressed)
	sp = shortest_path(compressed)
	#print(sp)
	#print(ng)
	#print(renode(sp,ng))
	path = retrace(sx,sy,sp,ng)
	#printee(edge_maze)
	compromise(edge_maze)
	#print("sx="+str(sx))
#	print("sy="+str(sy))
#	print("fx="+str(fx))
#	print("fy="+str(fy))
	#ans= distance(maze,sx,sy,fx,fy)
	#print ("the shortest path is "+ans+ " spaces")
	#et=strftime("%S", gmtime())
	#et = datetime.now()
	#et = et.microsecond
	#path = normal(path)
	write_tofile(sp,"ZShortest_Path.txt")
	write_tofile(ng,"ZNode_Graph.txt")
	write_tofile(edge_maze,"ZEdge_maze.txt")
	write_tofile(graph,"ZGraph.txt")
	#print("Completed in "+str(float(et)/1000000-float(st)/1000000)+" seconds.")
	path = restring(path,die)
	print(path)
	write_string(path)
	return path

def restring(path,die):
	lastc=path[0]
	amt=0
	redo=[]
	path+=path[len(path)-1]
	path+='0'
	np = ''
	for i in range(len(path)):
		#print(path[i])
		if path[i]!=lastc:
			div = 0
			if lastc=='r' or lastc=='l':
				amt=amt/(die[0]/3)
			if lastc=='u' or lastc=='d':
				amt=amt/(die[0]/3)
			for j in range(amt):
				np+=lastc
			#redo.append("("+lastc+","+str(amt)+")")
			
			lastc=path[i]
			amt=0
		else:
			amt+=1
	return np

def renode(sp,ng):
	final = []
	for i in range(len(sp)):
		final.append(ng[sp[i][0]])
	return final

def retrace(sx,sy,sp,ng):
	#print(sy,sx)
	fullstring=''
	for ele in sp:
		weep=''
		#print(ele)
		if ele[2]=='v':
			#print(ng[ele[0]])
			tmp = sy-ng[ele[0]][0]
			#print(tmp)
			if tmp<0:
				weep=weep+'d'*abs(tmp)
			if tmp>0:
				weep=weep+'u'*abs(tmp)
			tmp = sx-ng[ele[0]][1]
			#print(tmp)
			if tmp<0:
				weep=weep+'r'*abs(tmp)
			if tmp>0:
				weep=weep+'l'*abs(tmp)
			sy=ng[ele[0]][0]
			sx=ng[ele[0]][1]
		if ele[2]=='h':
			#print(ng[ele[0]])
			#print(ng[ele[0]])
			tmp = sx-ng[ele[0]][1]
			#print(tmp)
			if tmp<0:
				weep=weep+'r'*abs(tmp)
			if tmp>0:
				weep=weep+'l'*abs(tmp)
			tmp = sy-ng[ele[0]][0]
			#print(tmp)
			if tmp<0:
				weep=weep+'d'*abs(tmp)
			if tmp>0:
				weep=weep+'u'*abs(tmp)
			sy=ng[ele[0]][0]
			sx=ng[ele[0]][1]
		fullstring+=weep
		#print(weep)
	#print(fullstring)
	#print("UD")
	return fullstring


def normal(string):
	i=0
	ns = ''
	changed=False
	while i<len(string)-1:
		if (string[i]=='l' and string[i+1] == 'r') or (string[i]=='r' and string[i+1] == 'l') or(string[i]=='u' and string[i+1] == 'd') or (string[i]=='d' and string[i+1] == 'u'):
			tmp = string[:]
			string = tmp[:i]+tmp[i+2:]
			changed=True
			i-=2
		i+=1
	return string

def compress(graph,edges):
	directed = []
	for i in range(0,len(edges)):
		directed.append([i])
	for i in range(0,len(graph)):
		directed[graph[i][0]].append((graph[i][1],graph[i][2],graph[i][3]))
	for i in range(0,len(graph)):
		new = ''
		if graph[i][3]=='v':
			new='h'
		else:
			new='v'
		directed[graph[i][1]].append((graph[i][0],graph[i][2],new))
	return directed
		
def shortest_path(graph):
	dist = []
	previous = []
	current = 0
	dist.append(0)
	remaining=[]
	remaining.append(graph[0][0])
	previous.append([])
	for i in range(1,len(graph)):
		remaining.append(graph[i][0])
		dist.append(999999)
		previous.append([])
	while len(remaining)!=0:
		sss = find_smallest(dist,remaining)
		current=remaining[sss]
		remaining.pop(sss)
		for i in range(1,len(graph[current])):
			alt = dist[current]+graph[current][i][1]
			if alt<dist[graph[current][i][0]]:
				dist[graph[current][i][0]]=alt
				previous[graph[current][i][0]]=previous[current][:]
				previous[graph[current][i][0]].append(graph[current][i])
				#print(previous[current],alt)
				#time.sleep(.15)
	return previous[len(previous)-1]
	
def find_smallest(dist,remaining):
	smallest = 999999999999999
	ind = 0
	for i in range(0,len(remaining)):
		num = remaining[i]
		if dist[num]<smallest:
			smallest = dist[num]
			ind = i
	return ind
	
def get_nodes(ng,edge_maze,explored):
	i = 0
	j = 0
	nodes = []
	for i in range(0,len(ng)):
		for j in range(len(ng)):
			connected0 = True
			connected1 = True
			direction = 'v'
			if ((ng[i][0]<ng[j][0] and not findd(ng[i][1],ng[i][0],ng[j][0],edge_maze)) or (ng[i][1]>ng[j][1] and not findl(ng[j][0],ng[i][1],ng[j][1],edge_maze)) or (ng[i][0]>ng[j][0] and not findu(ng[i][1],ng[i][0],ng[j][0],edge_maze)) or (ng[i][1]<ng[j][1] and not findr(ng[j][0],ng[i][1],ng[j][1],edge_maze))):
				connected0 = False
				direction = 'h'
			if ((ng[i][1]<ng[j][1] and not findr(ng[i][0],ng[i][1],ng[j][1],edge_maze)) or (ng[i][1]>ng[j][1] and not findl(ng[i][0],ng[i][1],ng[j][1],edge_maze)) or (ng[i][0]>ng[j][0] and not findu(ng[j][1],ng[i][0],ng[j][0],edge_maze)) or (ng[i][0]<ng[j][0] and not findd(ng[j][1],ng[i][0],ng[j][0],edge_maze))):
				connected1= False
			if connected0 == True or connected1 == True :
				dis = abs(ng[i][0]-ng[j][0])+abs(ng[i][1]-ng[j][1])
				nodes.append((i,j,dis,direction))
	return nodes
	
def findu(x,s,d,maze):
	while s!=d:
		s=s-1
		if s== -1:
			return False
		if maze[s][x]==' 1':
			return False
		if maze[s][x]=='EE' and s!=d:
			return False
	return True
	
def findd(x,s,d,maze):
	while s!=d:
		s=s+1
		if s== len(maze):
			return False
		if maze[s][x]==' 1':
			return False
		if maze[s][x]=='EE' and s!=d:
			return False
	return True
	
def findl(y,s,d,maze):
	while s!=d:
		s=s-1
		if s== -1:
			return False
		if maze[y][s]==' 1':
			return False
		if maze[y][s]=='EE' and s!=d:
			return False
	return True
	
def findr(y,s,d,maze):
	while s!=d:
		s=s+1
		if s == len(maze):
			return False
		if maze[y][s]==' 1' :
			return False
		if maze[y][s]=='EE' and s!=d:
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
			if edges2[y][x] in ['-2','-3']:
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
	return skimp(edges),nodachi

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
	print('\n')
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
		
def get_maze():
	f = open ('maze.txt', 'r')
	test = str(f.read())
	d=[]
	test=str(test)
	tmp = ''
	tmpl=[]
	for i in range(0,len(test)):
		if test[i]=='\n' and tmp !='':
			d.append(tmpl)
			tmpl = []
			tmp=''
		if test[i]!='\n':
			tmpl.append(test[i])
			tmp+=test[i]
	if tmp!='':
		d.append(tmpl)
	return d

def write_tofile(output,filename):
	f = open(filename, 'w')
	f.seek(0)
	for ele in output:
		f.write(str(ele))
		f.write('\n')
	f.close();
	
def write_string(output):
	f = open('output', 'w')
	f.seek(0)
	f.write(output)
	f.close();
	
def compromise(maze):
	#print('\n')
	for ele in maze:
		ns=''
		for i in range(0,len(ele)):
			if ele[i]=='EE':
				ns+='E'
			if ele[i]==' 1':
				ns+='1'
			if ele[i]==' 0':
				ns+='0'
			if ele[i]==' 2':
				ns+='2'
			if ele[i]==' 3':
				ns+='3'
		#print(ns)
