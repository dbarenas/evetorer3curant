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
 
def preprocess_wiki(): 
	file1 = open('key_list_fit200', 'r')
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
			wok=','.join(wik[:200]) #implmentar el tf aqui
			gword.append(w[0])
			dict_cont[w[0]]=wok
	mean=[]
	for i in dict_cont.values():
		mean.append(i)

	return mean
	#************************************

def preprocess_wiki_values(): 
	file1 = open('key_list_fit200', 'r')
	#************************************
	gword=[]
	kword=[]
	dict_cont={}
	cnt=0
	mlist=[]
	for wtopic in file1.readlines():
		w=wtopic.split(":")
		mlist.append(w[0])
	return mlist

def preprocess_q_keyw(qtxt):
	#---
	qtxt_org=qtxt
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
			lre.append(i.lower())
	keyw=[]
	stpw=["navigation","search","about","http","edit","Intro","read","help","removed","above"]
	file1 = open('stop-words', 'r')
	for i in file1.readlines():
		stpw.append(i.strip())
	for i in lre:
			if i not in stpw:
	 			keyw.append(i)
	return keyw

def preprocess_q(qtxt_pre):
	#************************************
	brown_news_tagged = brown.tagged_sents(categories='news')
	brown_news_text = brown.sents(categories='news')
	tagger = nltk.UnigramTagger(brown_news_tagged[:5500])
	qttxt=qtxt_pre.split(',')
	wqtxt=qtxt_pre.split() 
	ttcontent= tagger.tag(wqtxt)
	ttw=[]
	for i in ttcontent:
		if i[1]:
			ttw.append(i[0])	
	#---
	keyw=preprocess_q_keyw(qtxt_pre)
	#---
	llw=""
	llw= ', '.join(ttw)
	lle=""
	lle= ','.join(keyw) 
	qtxt_pre=lle+","+llw
	return qtxt_pre
 	#---
	#************************************

def exsh(quest):
	qtxt=quest
 	mean=preprocess_wiki()
 	vectorizer = CountVectorizer(min_df=0,stop_words=None,ngram_range=(1 , 1))
 	X = vectorizer.fit_transform(mean)
 	#analyze = vectorizer.build_analyzer()
 	matrix = X.toarray()
	values=preprocess_wiki_values()
	mlist=values
	qtxt_q=preprocess_q(quest)
	idevent=quest.split(',')
	noua= qtxt_q.split(',')
	fcontent=[]
	fcontent.append(idevent[0])
	fcontent = [wip for wip in noua if re.sub(r'[^0-9A-Za-z]', "", wip)]
	 
	q=vectorizer.transform([qtxt_q]).toarray()
	qtr= zip(*q)
	qt = np.matrix(qtr)
	M,N = matrix.shape	
	U,s,Vh = linalg.svd(matrix)
	Sig = linalg.diagsvd(s,M,N)
	U, Vh = U, Vh
	# print U # -> is Vh
	# print Vh # -> is U
	ur=U.dot(Sig.dot(Vh))

	Uk= np.matrix(Vh)
	#si quisiera guardar la matriz de keywords deberia ser aqui en este lugar
	#Sigk=np.matrix([[ 1/4.0989,0., 0., 0., 0., 0., 0., 0., 0., 0.,0. ], [ 0., 1/2.3616,  0., 0., 0., 0., 0., 0., 0., 0.,0. ],[ 0.,0.,1/1.27197841,0.,0.,0.,0.,0.,0.,0.,0. ]])
	Sig=np.matrix(Sig)
	Sigk=Sig.getI()
	Sigk= Sigk.T
	qr=Sigk.dot(Uk)
	r=qr.dot(qt)

	qqr=zip(*r.tolist())
	qlen=len(qqr[0])

	k = 5 #Rango corte
	rus=fcontent[:10]
 	#rus=[]
	if k < qlen:
		#print "'-._.-'"
		for tr in range(len(U)):
			res=1-scipy.spatial.distance.cosine(U[tr][:k], qqr[0][:k])
			if res >= 0.8:
 				rus.append(mlist[tr])
	else:
		print "Pruna menor de k ...determina un elemento mayor"

	tot_res=[qtxt]
	tot_res.append(rus)	
	return tot_res #resultados titulo + palabras correlacionadas

#qtxt='12363 , Carabas Presents: Alternative Drinks (Music, Sci-fi, Film, Comics etc),enjoy along come friends invite ticket book etc art events bands comics books projects work attendees recommendations nostalgia clips wonderful weird screen plasma reel Film Visuals day present others Dance Rock Indie crowdpleaser system sound mix playlist Alternative Soundtrack room function venue Excellent drinks folk meeting enjoys thing kind like sounds thinks anyone frankly woes share ideas bounce work promote others meet professionals artists writers musicians creators like Comics fi Sci Style Music Alternative Film Cult life side alternative loves anyone night social ,1,Career and Life Balance,98,Music , 0'
#print exsh(qtxt)