n=0
for i in $(cat l4);do
	let n=n+1
	curl $i | grep pub-pbmap | grep -rv "/a" | sed 's/<a href="//g' | sed 's/">//g' >> l5 
done
