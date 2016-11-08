from bs4 import BeautifulSoup
import requests
import unicodedata
import lxml
import re
import string
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import csv
from nltk.tokenize import RegexpTokenizer
from collections import defaultdict


# Creates soup
soup = BeautifulSoup(open("ABSA15_Hotels_Test.xml"), "lxml-xml")


# Creates the dictionary holding tags/list of responses about said tags
tags_dict = defaultdict(list);

# Creates the dictionary holding the tags/tokenized items
token_dict = defaultdict(list);

# Gets all opinion tags
opinion = soup.find_all('Opinion')

# Gets all sentence tags (includes contents)
tagList = soup.find_all('sentence');

# Fills dict
for curr_tag in tagList:
    sentence = curr_tag.contents[1].contents
    for y in range(3, len(curr_tag) - 1):
        tags_dict[curr_tag.contents[y].contents[1]['category']].append(sentence);

# See contents of tag dictionary      
print (tags_dict);

# Fills up adjective dictionary with 
for key, review in tags_dict.items():
    for rev in review:
        rev_string = str(rev)
        tokenizer = RegexpTokenizer(r'\w+')
        tokenizer.tokenize(rev_string)
        tokenized_review = word_tokenize(str(rev))
        for i,j in nltk.pos_tag(tokenized_review):
            if j in ['JJ', 'JJR', 'JJS']:
                # add other POS tags to list above
                token_dict[key].append(i)
                
#S See contents of adjective dictionary
print (token_dict)
