import datetime
import re
import nltk
import mysql.connector
from HTMLParser import HTMLParser
from re import sub
from sys import stderr
from traceback import print_exc
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize
from nltk.corpus import stopwords


class _DeHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.__text = []

    def handle_data(self, data):
        text = data.strip()
        if len(text) > 0:
            text = sub('[ \t\r\n]+', ' ', text)
            self.__text.append(text + ' ')

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.__text.append('\n\n')
        elif tag == 'br':
            self.__text.append('\n')

    def handle_startendtag(self, tag, attrs):
        if tag == 'br':
            self.__text.append('\n\n')

    def text(self):
        return ''.join(self.__text).strip()


def dehtml(text):
    try:
        parser = _DeHTMLParser()
        parser.feed(text)
        parser.close()
        return parser.text()
    except:
        print_exc(file=stderr)
        return text

def orq(text):
	r=dehtml(text)
	rtoken= wordpunct_tokenize(r)
	stopwords = nltk.corpus.stopwords.words('english')
	content = [w for w in rtoken if w.lower() not in stopwords]
	fcontent = [w for w in content if re.sub(r'[^A-Za-z]', "", w)]
        other=""
        gcontent=[]
        for i in fcontent:
            other=str(i)+" "+other
        gcontent.append(other)
	return other

# rmlist=["today","p","date","recognition","aims","it"]
# tcontent = [w for w in fcontent if w.lower() not in rmlist]

#::: Genera la conexion a la base de datos pickevent_production-webapp  :: pickevent2dot0
cnx = mysql.connector.connect(user='root',password='root',host='127.0.0.1',port='8889', database='pickevent_production-webapp')

#::: el cursor de esa consulta
cursor = cnx.cursor()

#la consulta inicial que me entrega datos con loque puedo trabajar
#query = ("SELECT e.id, e.title, e.description, e.topic_id, t.name AS topic, e.industry_id, ind.name as industry, e.category_id AS cat FROM events AS e LEFT JOIN topics AS t ON t.id = e.topic_id LEFT JOIN industries AS ind ON e.industry_id = ind.id")
query = ("SELECT e.id, e.title, e.description, e.topic_id, t.name AS topic, e.industry_id, ind.name as industry, e.category_id AS cat, e.location_id, e.price, e.price_comments, e.start_time,e.end_time FROM events AS e LEFT JOIN topics AS t ON t.id = e.topic_id LEFT JOIN industries AS ind ON e.industry_id = ind.id")
cursor.execute(query)

#0-e.id
#1-e.title
#2-e.description
#3-e.topic_id
#4-t.topic_name
#5-e.industry_id
#6-ind.industry_name
#7-e.category_id
#8-e.price
#9-e.price_comments
#10-e.start_time
#11-e.end_time

#envio a un array toda la informacion : podria ser un diccionario
event=[]
a=""
for i in cursor:
    event.append(i[0])
    trs=i[2].encode('utf-8')
    a=orq(trs) 
    #limpia el html
    tot= i[1].encode('utf-8')+","+str(a)+","+str(i[11])+","+str(i[12])+",cat:"+str(i[7])+","+str(i[3])+","+str(i[4])+","+str(i[5])+","+str(i[6])+","+str(i[8])+","+str(i[9])
    event.append(tot)

#instancio otro cursor sobre la misma conexion
#print ":::"*20
cursore = cnx.cursor()
query2 = ("SELECT e.id, t.name AS topic, ets.topic_id FROM events AS e  INNER JOIN events_to_sub_topics AS ets ON e.id = ets.event_id LEFT JOIN topics AS t ON t.id = ets.topic_id")
cursore.execute(query2)
subtopic=[]
for m in cursore:
 	subtopic.append(m[0])
 	subtopic.append(m[1].encode('utf-8'))

eventcount=len(event)
for tr in range(0,eventcount,2):
	l=0
 	co=len(subtopic)
 	sub=[]
 	er=0
 	for l in range(co):
 		if subtopic[l] == event[tr]:
 			er=subtopic[l+1]
 			sub.append(er)
 	#print event[tr],",",event[tr-1],",",er

#print ":::"*20
cursore = cnx.cursor()
query2 = ("SELECT e.id, t.name AS topic, ets.topic_id FROM events AS e  INNER JOIN events_to_sub_topics AS ets ON e.id = ets.event_id LEFT JOIN topics AS t ON t.id = ets.topic_id")
#SELECT e.start_time,e.end_time,e.id, e.title, e.description, e.topic_id,t.name AS topic,e.location_id, e.price, e.price_comments, e.industry_id, ind.name as industry FROM events AS e LEFT JOIN topics AS t ON t.id = e.topic_id LEFT JOIN industries AS ind ON e.industry_id = ind.id where e.topic_id=2 and ind.name like "%and%"

cursore.execute(query2)
subtopic=[]
for m in cursore:
 	subtopic.append(m[0])
 	subtopic.append(m[1].encode('utf-8'))

eventcount=len(event)
for tr in range(0,eventcount,2):
	l=0
 	co=len(subtopic)
 	sub=[]
 	er=0
 	for l in range(co):
 		if subtopic[l] == event[tr]:
 			er=subtopic[l+1]
 			sub.append(er)
 	print event[tr],",",event[tr-1],",",er

cursor.close()
cnx.close()