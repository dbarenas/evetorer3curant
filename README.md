evetorer3curant
===============


Hibrid Recomender System for Events   “Event Curator”

"Getting context of eventbrite events for produce a efective event recomendations matchin the skill info of the users on linkedin"


This is a master degree project thesis and a model product for Pickevent.com
The License is GPL v2



* In the file Aproximation_1 you can found the suficient source for getting a classification process of a event_list files.
* This system depends of a secondary system who index the results of the principal data with the classifications results, clasification of a event and the clasificaion of a user skills mathched gives a recomendation.
* 

For use this read the next instructions.

'''STEP 1'''

Install 
<code>

    apt-get install python-nltk python-num python-scipy
    apt-get install python-nltk 
    apt-get install cython
</code>

<code>

    apt-get install git
    git clone git://github.com/scikit-learn/scikit-learn.git
    cd scikit-learn/
    python setup.py build_ext --inplace
    cd ..
    cd scikit-learn/
    python setup.py install
</code>

<code>

    cd beautifulsoup4-4.3.1/
    python setup.py install    

</code>

Download wikiapi or install via pip
<code>  

    sudo pip install wikiapi
</code>

Now goin to aproximation_1 and execute clasificator_tester.py  this clasificator going to classify the events_list file into a topic and industry words, this words have a dictionary with the classification of the wikipedia.

And wuala! now you have a event classified.

Now you can use a base of id_users, skills (s1,s2,s3,s4) and classify over the same word with dictionary list.

With this classifications you have a layer with the context and you can match the similarities into users and information provides about a event.

If you wanna reuse this with your data base and need help, please contact with me dabuiar[AT]gmail[dot]com. 


