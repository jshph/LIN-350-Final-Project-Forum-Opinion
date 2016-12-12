import nltk
from nltk.tokenize import RegexpTokenizer
import operator
from nltk.tokenize import word_tokenize



tokenizer = RegexpTokenizer(r'\w+')

file = open("textrank_hotels_output2.txt", "r")
data = dict()
dictList = [];
dictNumber = 0;

# counts 
for line in file:
    if line.strip():
        word = tokenizer.tokenize(line)
        if len(word) > 0:
            if (word[0].isupper()):
                dictList.append(data)
                data = dict()
                data[line] = 0
                continue
##            if word[0] not in data:
##                data[word[0]] = 1
##            else:
##                data[word[0]] = data[word[0]] + 1
            for single in word:
                if not single.isdigit():
                    if single not in data:
                        data[single] = 1
                    else:
                        data[single] = data[single] + 1
                    

# print (dictList)


for dataset in dictList:
    dataset2 = dict(dataset);
    for item in dataset2:
        if len(item) == 1:
            del dataset[item]



for dataset in dictList:
    sorted_data = sorted(dataset.items(), key=operator.itemgetter(1))
    for line in sorted_data:
        if line[0].isupper():
            print ("\n")
            print (line[0])
            print ("\n")
        else:
            print(line)

##data2 = dict(data)
##
### filtering:
### 1. number of instances
### 2. manual items
### 3. parsing issue
### 4. non-nouns
##for item in data2:
##    if data[item] < 3:
##        del data[item]
##    elif "hotel" in item or "stay" in item or "excellent" in item or "phoenix" in item or "tablet" in item or "android" in item or "free" in item or "book" in item or "mount" in item or "page" in item:
##        del data[item]
##    elif len(item) == 1:
##        del data[item]
##    else:
##        text = word_tokenize(item)
##        sample_line = nltk.pos_tag(text)
##        if sample_line[0][1] not in 'NN':
##            del data[item]
##    
### sorts dict for printing
##sorted_data = sorted(data.items(), key=operator.itemgetter(1))
##
##for line in sorted_data:
##    print(line)
