n=0
for i in $(cat l3);do
	let n=n+1
	curl $i | grep pub-pbmap | grep -rv "/a" | sed 's/<a href="//g' | sed 's/">//g' >> l4 
done
