from sklearn.feature_extraction.text import CountVectorizer
from scipy import linalg,array,dot,mat,spatial
import nltk
from nltk.tokenize import *
from nltk.corpus import stopwords
from nltk.corpus import brown
from math import *
import numpy as np
import scipy
import sys
import re
import operator
import unicodedata
import urllib
import urllib2
from wikiapi import WikiApi
from bs4 import BeautifulSoup
  
file1 = open('key_list_fit100', 'r')
#************************************
gword=[]
kword=[]
dict_cont={}
cnt=0
mlist=[]
for wtopic in file1.readlines():
	w=wtopic.split(":")
	mlist.append(w[0])
 	if w[0] not in gword:
		cnt=cnt+1
		wik=w[1].split(',')
		wok=', '.join(wik[:100]) #implmentar el tfidf aqui
		gword.append(w[0])
		dict_cont[w[0]]=wok
		
 		#print cnt,w[0],wok
	    #print w[0],":",w[1]  

     
 	#implementation of encoder and put all the words in lower case
	# gcontent=[]
	# for i in fcontent:
	# 	gcontent.append(i.encode('utf-8').lower())
	# 	er=""
	# er= ', '.join(gcontent)
	# 	dic_cont[w[0]]=er+","+llw
#************************************

mean=[]
for i in dict_cont.values():
	mean.append(i)

#*********************************************************************************

vectorizer = CountVectorizer(min_df=0,stop_words=None,ngram_range=(1 , 1))
X = vectorizer.fit_transform(mean)
# print ";*;"*50
# print X
# print ";*;"*50
analyze = vectorizer.build_analyzer()

# print "*"*20
#print vectorizer.get_feature_names()
# print "*"*20
matrix = X.toarray()
###print matrix

#qtxt='12213 , DESIGN AND PRINT YOUR OWN TOTE BAG: SESSION 1,email foot link click simply time unsubscribe wish Art Cass coming updated keep list email events come people add usually note Please time session preferred book sure make Please information cover day sessions advance booked must tickets capacity Limited com dovilep www team Art Cass part Hackney heart studio works design layout books art edition limited collage printing screen specialising London artist graphic Puzinaite Dovile wear apron clothing old bring please clothes staining avoid provided materials bags Tote paper printing try bag tote Print stencils made pre selection using fabric printing screen process explain Puzinaite Dovile artist workshop introductory fabric print screen learn Want FABRIC PRINTING SCREEN INTRODUCTION ,56,Information Technology,1,All , 0'
#qtxt='12378 , Be your own coach,us find time extra allow please Library Business City visit first attendance ensure seminars charge forced cancelling without day attend seminars book continue people note Please effectiveness professional personal enhance important identify learn make want changes towards work identify help tool coaching powerful use show workshop practical Mina Maria SPEAKER NEW coach ,75,Marketing and Sales,1,All , 0'
brown_news_tagged = brown.tagged_sents(categories='news')
brown_news_text = brown.sents(categories='news')
tagger = nltk.UnigramTagger(brown_news_tagged[:5500])

#qtxt='12363 , Carabas Presents: Alternative Drinks (Music, Sci-fi, Film, Comics etc),enjoy along come friends invite ticket book etc art events bands comics books projects work attendees recommendations nostalgia clips wonderful weird screen plasma reel Film Visuals day present others Dance Rock Indie crowdpleaser system sound mix playlist Alternative Soundtrack room function venue Excellent drinks folk meeting enjoys thing kind like sounds thinks anyone frankly woes share ideas bounce work promote others meet professionals artists writers musicians creators like Comics fi Sci Style Music Alternative Film Cult life side alternative loves anyone night social ,1,Career and Life Balance,98,Music , 0'
qtxt='DESIGN AND PRINT YOUR OWN TOTE BAG SESSION 1,email foot link click simply time unsubscribe wish Art Cass coming updated keep list email events come people add usually note Please time session preferred book sure make Please information cover day sessions advance booked must tickets capacity Limited com dovilep www team Art Cass part Hackney heart studio works design layout books art edition limited collage printing screen specialising London artist graphic Puzinaite Dovile wear apron clothing old bring please clothes staining avoid provided materials bags Tote paper printing try bag tote Print stencils made pre selection using fabric printing screen process explain Puzinaite Dovile artist workshop introductory fabric print screen learn Want FABRIC PRINTING SCREEN INTRODUCTION ,56,Information Technology,1,All , 0'
wqtxt=qtxt.split()
  
ttcontent= tagger.tag(wqtxt)
ttw=[]
for i in ttcontent:
	if i[1]:
		ttw.append(i[0])	
#	if i[1] == "NN" or i[1] == "VB" or i[1] == "JJ":
#		ttw.append(i[0])
#---
ws=qtxt.split()
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

 #---

 
llw=""
llw= ', '.join(ttw)
 
qtxt=llw

print qtxt


#'Organizing an Effective Remote Deposit Capture Compliance Program,Managers Risk Officers Technology Chief Auditors Officers Compliance Officers Management Cash Treasury Officers Operations Deposit Officer Banking Electronic Officers Services RDC Attend findings examination top five Discover guidelines FFIEC parallel documentation management risk RDC Organizing management risk assessment examiner Explanation Program Compliance Capture Deposit Remote Effective Organizing ,30,Finance and Banking,13,Banking , 0'

#qtxt='Finance'

q=vectorizer.transform([qtxt]).toarray()
# print "q *"*20
qtr= zip(*q)
qt = np.matrix(qtr)

M,N = matrix.shape

U,s,Vh = linalg.svd(matrix)

Sig = linalg.diagsvd(s,M,N)
U, Vh = U, Vh
# print "u."*20
# print U # -> is Vh
# print "S."*20
# print Sig
# print "Vh."*20
# print Vh # -> is U
ur=U.dot(Sig.dot(Vh))

# print "experimento"
Uk= np.matrix(Vh)
#Sigk=np.matrix([[ 1/4.0989,0., 0., 0., 0., 0., 0., 0., 0., 0.,0. ], [ 0., 1/2.3616,  0., 0., 0., 0., 0., 0., 0., 0.,0. ],[ 0.,0.,1/1.27197841,0.,0.,0.,0.,0.,0.,0.,0. ]])
Sig=np.matrix(Sig)
Sigk=Sig.getI()
Sigk= Sigk.T
# print type(qt)
# print qt.shape
# print type(Uk)
# print Uk.shape
# print type(Sigk)
# print Sigk.shape
#qr=(qt)dot(Uk)dot(Sk)exp-1
# print ":"*20
qr=Sigk.dot(Uk)
# print qr.shape
# print "R"*20
r=qr.dot(qt)
###print "el vector q=",r.tolist()

#print ":R:"*20
# for i in U:
# 	print i[:6]
 
qqr=zip(*r.tolist())
qlen=len(qqr[0])
# print len(qqr[0])
# print qqr[0][:3]

k=5 # Rango corte
if k < qlen:
	print "'-._.-'"
	for tr in range(len(U)):
		res=1-scipy.spatial.distance.cosine(U[tr][:k], qqr[0][:k])
		if res >= 0.9:
			print mlist[tr]
			#," d"+str(tr)," = ",res," ::: "
			#, dict_cont[mlist[tr]]
else:
	print "Pruna menor de k ...determina un elemento mayor"

