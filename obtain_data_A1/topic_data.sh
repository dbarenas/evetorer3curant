
#! / bin / bash           

while read line           
do      
	echo "**********"
	echo $line     
	python pinkiwiki.py $line    
done < mlist
