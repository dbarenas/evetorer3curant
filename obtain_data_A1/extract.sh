
#! / bin / bash           

while read line           
do      
	echo $line
	curl http://en.wikipedia.org/wiki/$line | html2text | head -1000 > top/$line      
#	python pinkiwiki.py $line    
done < topics_list
