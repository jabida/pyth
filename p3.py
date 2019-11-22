import re
f=open("manifest.xml","r+")
f2=open("out.txt","w+")
for i in f:

	s=re.sub(">","#",i)	

	f2.write(s)

f2.seek(0,0)
f3=open("out.txt2","w")
for k in f2:

	rs=re.sub("<","$",k)
    	
        f3.write(rs)
f.close()
f2.close()
f3.close()                                                                                          
             
