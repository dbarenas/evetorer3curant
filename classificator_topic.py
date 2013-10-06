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
  
file1 = open('mlist', 'r')
#************************************
# INIT FUNCTION lalawiki(searchword)
#************************************
def lalawiki(searchword):
	article= searchword
	article = urllib.quote(article)

	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')] #wikipedia needs this

	resource = opener.open("http://en.wikipedia.org/wiki/" + article)
	data = resource.read()
	resource.close()
	soup = BeautifulSoup(data)
	#print soup.find('div',id="bodyContent").p
	a=soup.findAll('a',recursive=True,limit=500)

	brown_news_tagged = brown.tagged_sents(categories='news')
	brown_news_text = brown.sents(categories='news')
	tagger = nltk.UnigramTagger(brown_news_tagged[:5500])

	l=[]
	for i in a:
		l.append(i)

	tot=[]
	for n in l:
		for r in n:
			nn=r.encode('utf-8')
			tot.append(nn)

	fcontent = [wip for wip in tot if re.sub(r'[^A-Za-z]', "", wip)]

	ttcontent= tagger.tag(fcontent)
	keyw=[]
	for i in ttcontent:
		if "<" not in i[0] and "edit" not in i[0] and "navigation" not in i[0] and "search" not in i[0]:
			keyw.append(i[0])

	return keyw 
#************************************
#************************************
	
wiki = WikiApi({})
dic_cont={}
n=0
mlist=[]
lr=[]
#************************************

for wtopic in file1.readlines():
	w=wtopic.split()
 	mlist.append(w[0])
	results = wiki.find(w[0])
	if results:
		lr= lalawiki(w[0])
		llw=""
 		llw= ', '.join(lr)

		article = wiki.get_article(results[0])
 		r=article.content 
 		rtoken= wordpunct_tokenize(r)
 		
 		#implementation of stopwords
		stopwords = nltk.corpus.stopwords.words('english')
		content = [wip for wip in rtoken if wip.lower() not in stopwords]
		#implementation if there are a characters into the system
		fcontent = [wip for wip in content if re.sub(r'[^A-Za-z]', "", wip)]

		#implementation of encoder and put all the words in lower case
		gcontent=[]
		for i in fcontent:
			gcontent.append(i.encode('utf-8').lower())

		# # implements the tagger 
		# brown_news_tagged = brown.tagged_sents(categories='news')
		# brown_news_text = brown.sents(categories='news')
		# tagger = nltk.UnigramTagger(brown_news_tagged[:5500])
		# tagcontent= tagger.tag(fcontent)
 	# 	for i in tagcontent:
 	# 		#selects and index the interesting words on the same array
 	# 		j=re.match(r'J', str(i[1]))
		# 	n=re.match(r'N', str(i[1]))
		# 	v=re.match(r'V', str(i[1]))
 	# 		if j:
 	# 			gcontent.append(i[0].encode('utf-8'))
		# 	if n:
 	# 			gcontent.append(i[0].encode('utf-8'))
		# 	if v:
 	# 			gcontent.append(i[0].encode('utf-8'))

		#HEY! check this in this case im repeat the data 
		#im need to work in implements less info in the classification 

 		er=""
		er= ', '.join(gcontent)
  		dic_cont[w[0]]=er+","+llw
#************************************

#print dic_cont

mean=[]
for i in dic_cont.values():
	mean.append(i)


#*********************************************************************************

vectorizer = CountVectorizer(min_df=0,stop_words=None,ngram_range=(1, 1))
X = vectorizer.fit_transform(mean)
# print ";*;"*50
# print X
# print ";*;"*50
analyze = vectorizer.build_analyzer()

# print "*"*20
#print vectorizer.get_feature_names()
# print "*"*20
matrix = X.toarray()
# print matrix
qtxt='Organizing an Effective Remote Deposit Capture Compliance Program,Managers Risk Officers Technology Chief Auditors Officers Compliance Officers Management Cash Treasury Officers Operations Deposit Officer Banking Electronic Officers Services RDC Attend findings examination top five Discover guidelines FFIEC parallel documentation management risk RDC Organizing management risk assessment examiner Explanation Program Compliance Capture Deposit Remote Effective Organizing ,30,Finance and Banking,13,Banking , 0'
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
print "el vector q=",r.tolist()

#print ":R:"*20
# for i in U:
# 	print i[:6]
 
qqr=zip(*r.tolist())
qlen=len(qqr[0])
# print len(qqr[0])
# print qqr[0][:3]

k=3 # Rango corte
if k < qlen:
	print "'-._.-'"
	for tr in range(len(U)):
		print mlist[tr]," d"+str(tr)," = ",1-scipy.spatial.distance.cosine(U[tr][:k], qqr[0][:k])
else:
	print "Determina un rango menor"

