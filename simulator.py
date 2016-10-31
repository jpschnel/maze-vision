import time 
import os
import sys
def main():
	maze = get_maze()
	string = get_string() 
	print(string)
	sx=0
	sy=0
	dx=0
	dy=0
	for x in range(0,len(maze)):
		for y in range(0,len(maze[0])):
			if maze[x][y] == '2':
				sx=x
				sy=y
			if maze[x][y] == '3':
				dx=x
				dy=y
	print(sx,sy,dx,dy)
	maze[sx][sy]='X'
	print(string)
	time.sleep(2)
	for i in range(0,len(string)-1):
		if string[i]=='l':
			sy-=1
		if string[i]=='r':
			sy+=1
		if string[i]=='u':
			sx-=1
		if string[i]=='d':
			sx+=1
		maze[sx][sy]='X'
		sys.stderr.write("\x1b[2J\x1b[H")
		printeint(maze)
		print(i,string[i])
		time.sleep(.05)
	
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
	
def printeint(what):
	print('\n')
	for ele in what:
		ns=''
		for i in range(0,len(ele)):
			if ele[i]=='1':
				ns+=u'\u2588'
			if ele[i]=='0':
				ns+=' '
			if ele[i]=='2':
				ns+='2'
			if ele[i]=='X':
				ns+='X'
			if ele[i]=='3':
				ns+='3'
		print(ns)

def get_maze():
	f = open ('maze.txt', 'r')
	test = str(f.read())
	d=[]
	test=str(test)
	tmp = ''
	tmpl=[]
	for i in range(0,len(test)):
		if test[i]=='\r' and tmp !='':
			d.append(tmpl)
			tmpl = []
			tmp=''
		if test[i]!='\n' and test[i]!='\r':
			tmpl.append(test[i])
			tmp+=test[i]
	if tmp!='':
		d.append(tmpl)
	return d
	
def get_string():
	f = open ('output', 'r')
	return f.read()
	
def compromise(maze):
	print('\n')
	for ele in maze:
		ns=''
		for i in range(0,len(ele)):
			if ele[i]=='EE':
				ns+='E'
			if ele[i]==1:
				ns+=u'\u2588'
			if ele[i]==' 0':
				ns+=' '
			if ele[i]==' 2':
				ns+='2'
			if ele[i]==' 3':
				ns+='3'
		print(ns)
	
main()