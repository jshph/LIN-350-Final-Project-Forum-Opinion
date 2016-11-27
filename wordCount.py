import nltk
from nltk.tokenize import RegexpTokenizer
import operator
from nltk.tokenize import word_tokenize



tokenizer = RegexpTokenizer(r'\w+')

file = open("testoutput.txt", "r")
data = dict()

# counts 
for line in file:
     if line.strip():
        word = tokenizer.tokenize(line)
        if word[0] not in data:
            data[word[0]] = 1
        else:
            data[word[0]] = data[word[0]] + 1

data2 = dict(data)

# filtering:
# 1. number of instances
# 2. manual items
# 3. parsing issue
# 4. non-nouns
for item in data2:
    if data[item] < 5:
        del data[item]
    elif "tv" in item or "books" in item or "kindle" in item or "nook" in item or "tablet" in item or "android" in item or "free" in item or "book" in item or "mount" in item or "page" in item:
        del data[item]
    elif len(item) == 1:
        del data[item]
    else:
        text = word_tokenize(item)
        sample_line = nltk.pos_tag(text)
        if sample_line[0][1] not in 'NN':
            del data[item]
    
# sorts dict for printing
sorted_data = sorted(data.items(), key=operator.itemgetter(1))

for line in sorted_data:
    print(line)
