import re
f=open("manifest.xml","r")
for i in f:
    s=re.search("fetch.*$",i)
    if s:
    	break
print(s.group())
