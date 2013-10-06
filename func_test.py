import re

a="RE Mi aerfd LA la"
ws=a.split()
print ws
i=''
lr=[]
for i in ws:
	j=''
	for j in i:
		if j.isupper():
			lr.append(i)
 			i=''
lre=[]			
for i in lr:
	if i:
		lre.append(i)

print lre

 