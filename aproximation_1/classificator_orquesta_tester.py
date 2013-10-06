import sys
import classificator_one as recomienda
import pysolr
import codecs

# Setup a Solr instance. The timeout is optional.
solr = pysolr.Solr('http://localhost:8983/solr/', timeout=10)

file1 = open(sys.argv[1], 'r')
#sys.argv[1]
cnt=0
if __name__ == "__main__":
	for i in file1.readlines():
		cnt=cnt+1
                ups=unicode(i, errors='ignore')	
		a=recomienda.exsh(ups)
		event= a[0].split(',')
		#event=a[0].split()
		id_event=event[0]
		title=event[1]
		description=event[2]
		print id_event
		print title
		print description
		print a[1]
		# solr.add([{
  #       		"id": id_event,
		# 	"description": a[0],
  #       		"cat": a[1],
		# }
		# ])
		print "OK ",cnt
		
# solr.optimize()
