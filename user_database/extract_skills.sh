

for i in $(cat l5);do
	
	echo $i >> skill_list
	curl $i | grep miniskill | sed 's%<span class="miniprofile-container jellybean http://www.linkedin.com/skills/api/v1/miniskill/%%g' | sed 's/?proficiency=">//g' | sed 's/  //g' >> skill_list

done
