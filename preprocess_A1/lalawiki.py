import urllib
import urllib2
from bs4 import BeautifulSoup
from nltk.corpus import brown
import nltk
import re
import operator 

def lalawiki(searchword):
	article= searchword
	article = urllib.quote(article)

	opener = urllib2.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')] #wikipedia needs this

	resource = opener.open("http://en.wikipedia.org/wiki/" + article)
	data = resource.read()
	resource.close()
	soup = BeautifulSoup(data)
	l=soup.body.get_text()
	aenc= l
	a= aenc.split()
 	#---
	ws=a
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
			lre.append(i.lower())
	keyres=[]
	stpw=["wikipedia","navigation","search","about","http","edit","Intro","read","help","removed","above"]
	file1 = open('stop-words', 'r')
	for i in file1.readlines():
		stpw.append(i.strip())
	for i in lre:
			if i not in stpw:
	 			keyres.append(i)
#---
	noua=[]
	fcontent = [wip for wip in keyres if re.sub(r'[^A-Za-z]', "", wip)]

	for i in fcontent:
		noua.append(i)
 	a=noua
 	#print soup.findAll('a',recursive=True,limit=500)
	#a=soup.findAll('a',recursive=True,limit=500)
 
	brown_news_tagged = brown.tagged_sents(categories='news')
	brown_news_text = brown.sents(categories='news')
	tagger = nltk.UnigramTagger(brown_news_tagged[:5500])

	l=[]
	for i in a:
		l.append(i.encode('utf-8'))
 
	fcontent = [wip for wip in l if re.sub(r'[^A-Za-z]', "", wip)]
 	ttcontent= tagger.tag(fcontent)
	restagcont=[]
  	for i in range(len(ttcontent)):
 	 	if ttcontent[i][1]:
	 		#print ttcontent[i][0],":",ttcontent[i][1]
	 		restagcont.append(ttcontent[i][0].lower())
  	keyw=[]
  	stpw=["navigation","search","about","http","edit","Intro","read","help","removed","above"]
 	for i in restagcont:
		if i not in stpw:
 			keyw.append(i)

	return keyw
 
query="Sales" 
rel=lalawiki(query)
#print rel
drel={}
sortdrel=[]
for i in rel:
	#print i,":",rel.count(i)
	drel[i]=rel.count(i)
	sortdrel=sorted(drel.items(), key=operator.itemgetter(1))
listsort=[]

tm=len(sortdrel)
for i in range(tm-1,0,-1):
	listsort.append(sortdrel[i][0])

#print listsort
wok=', '.join(listsort)
print query,":",wok

