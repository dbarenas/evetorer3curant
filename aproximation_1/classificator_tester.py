import sys
import classificator_one as recomienda

file1 = open('event_list', 'r')
#sys.argv[1]
if __name__ == "__main__":
	for i in file1.readlines():	
		a=recomienda.exsh(i)
		event=a[0].split()
		id_event=event[0]
		print id_event
		print a[1]