from nltk.stem import *
stemmer = SnowballStemmer("english")
lemmer = LancasterStemmer()
sentence = "this is a sentence sentence"
words = sentence.split()
dictionary1 = {}
dictionary2 = {}

for w in words:
    w = stemmer.stem(w)
    if w in dictionary1:
        dictionary1[w] = dictionary1[w]+1;
    else:
        dictionary1[w] = 1
for w in words:
    w = lemmer.stem(w)
    if w in dictionary2:
        dictionary2[w] = dictionary2[w]+1;
    else:
        dictionary2[w] = 1
s = str("\"articleID\",\"title\", wordcount, " + str(dictionary1) + " , " + str(dictionary2))
print(s)

with open('output.csv','w') as f:
    for line in s:
        f.write(line)

