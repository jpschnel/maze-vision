import img_translator as it
import maze_vision_algo as mvsp
import os
import string

def main():
   f=open('config.txt','r')
   line = f.next()
   strpi=line
   strpi.replace('\n','')
   print(strpi)
   rad = it.trans_main()
	#print(rad)
   p = mvsp.mvsp(rad)
   #this=spur.SshShell(hostname="192.168.1.17", username="pi", password= "maze")
   #os.system('ssh pi@192.168.1.17')
   #os.system('ssh pi@192.168.1.17 | python maze-vision-driving_dev/Florence/Solve_Path')
   #this.run(['cd maze-vision-driving_dev/Florence'])
   #this.run(['python Solve_Path '+str(p)])
   os.system('ssh pi@'+strpi+' python maze-vision-driving_dev/Florence/Solve_Path.py '+str(p))
   print('done!')


main()
