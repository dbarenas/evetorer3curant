
#if you use a CSV  export use this 
head  -1 $1 | html2text | sed 's%","% "***" %g' > pre

#head  -1 events_to_sub_topics.csv | html2text | sed 's%","% "***" %g' > pre


# if oyu use a XML export of the database use this
#cat  events_to_sub_topicsxmle.xml | sed 's/&lt;//g' | sed 's/&quot;//g' | sed 's/&gt;//g' | sed 's/;/     /g' | sed 's/LISPAN STYLE=font-size://g' | sed 's/ small //g' | sed 's/font-family://g' | sed 's/arial,helvetica,sans-serif//g' | sed 's/DIVSPAN//g' | sed 's/STYLE//g' | sed 's/font-size//g' | sed 's/PSPAN//g' | sed 's/=://g' | sed 's/=//g' | sed 's/://g' | sed 's%BR/SPAN/DIV% %g' | sed 's%/UL%%g' |sed 's/UL//g' | sed 's%/SPAN%%g' | sed 's%/STRONG%%g' | sed 's%/SPAN%%g' | sed 's%BR/% %g' | sed 's/SPAN//g'

cat pre | sed 's/STRONG//g' | sed 's%/P%%g' | sed 's% P%%g' | sed 's%/LI%%g' | sed 's/ALT//g' > pre2


