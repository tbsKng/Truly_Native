import os 
import glob

Path=raw_input("Define Path: ")

for filename in glob.glob(os.path.join(Path, '*.txt')):
	f=filename
	#f=open(filename,'r')
	#print f.read()
	name=os.path.splitext(f)[0]
	os.rename(f,name+".html")
	#f.close()
