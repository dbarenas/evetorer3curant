import sys
import nltk

#file1 = open(sys.argv[1], 'r')
file1 = open('../test_pre', 'r')

cont=1
A=[]
lineaA=0
final=[]
for lineA in file1.readlines():	
	A=lineA.split(':*:')
	for i in A:
		r=i.split(' ')
		for j in r:
			if j == '"***"':
				final.append('BOOOOOOOOOOOM')	
			else:
				final.append(j)
	
for i in final:	
	print freqDist(i)	
print final	
