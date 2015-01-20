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
#tot  
file1 = open('tot', 'r')
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
#************************************
#************************************
	
wiki = WikiApi({})
dic_cont={} #diccionary
mlist=[] #word base
#************************************

for wtopic in file1.readlines():
	w=wtopic.split()
 	mlist.append(w[0])
	results = wiki.find(w[0])
	if results:

		article = wiki.get_article(results[0])
 		r=article.content 
 		rtoken= wordpunct_tokenize(r)
 		
 		#implementation of stopwords
		stopwords = nltk.corpus.stopwords.words('english')
		content = [wip for wip in rtoken if wip.lower() not in stopwords]
		#implementation if there are a characters into the system
		fcontent = [wip for wip in content if re.sub(r'[^A-Za-z]', "", wip)]
		gcontent=[]
		for i in fcontent:
			gcontent.append(i.encode('utf-8').lower().strip())

 		drel={}
		for i in gcontent:
			#print i,":",rel.count(i)
			drel[i]=gcontent.count(i)
			sortdrel=sorted(drel.items(), key=operator.itemgetter(1))
		wikisort=[]

		tm=len(sortdrel)
		for i in range(tm-1,0,-1):
			wikisort.append(sortdrel[i][0])


		#-- START Keywords by url --
		rel=lalawiki(w[0])
		#print rel
		drel={}
		for i in rel:
			#print i,":",rel.count(i)
			drel[i]=rel.count(i)
			sortdrel=sorted(drel.items(), key=operator.itemgetter(1))
		listsort=[]

		tm=len(sortdrel)
		for i in range(tm-1,0,-1):
			listsort.append(sortdrel[i][0])

		#print listsort
		llw=', '.join(listsort)
 		#--- END ---

		#HEY! check this in this case im repeat the data 
		#im need to work in implements less info in the classification 

 		er=""
		er= ','.join(wikisort[:300])
  		dic_cont[w[0]]=llw+","+er
  		#print w[0],":",er+","+llw
  		print w[0],":",llw+","+er
#************************************




