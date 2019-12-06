import re

f=open("manifest.xml",'r')


 
count = 0

for i in f:
	r=re.match("path",i) 
	if r == "path": 
		count = count + 1
		print(count) 
 
