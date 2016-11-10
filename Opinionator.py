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

# used for binning up all categories for the adjectives they occur with
def rec_dd():
    return defaultdict(int)
adj_to_category = defaultdict(rec_dd)

# binning up all adjectives for the categories they occur with
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
                adj_to_category[i][key] += 1

                
#See contents of adjective dictionary
# print (token_dict)

# 
for adj, cats in adj_to_category.items():
    sorted_categories = sorted(list(cats.items()), reverse=True, key=lambda x: x[1])
    print(adj)
    for x in sorted_categories:
        print ('\tin ', x[0], x[1], 'times')

"""
example output:
annoying
    in  FACILITIES#QUALITY 1 times
hassle-free
    in  FACILITIES#GENERAL 1 times
friendly
    in  SERVICE#GENERAL 7 times
    in  ROOMS#CLEANLINESS 1 times
inexpensive
    in  HOTEL#PRICES 1 times
    in  HOTEL#GENERAL 1 times
clean
    in  ROOMS#CLEANLINESS 3 times
    in  SERVICE#GENERAL 3 times
    in  ROOMS#GENERAL 2 times
    in  FACILITIES#GENERAL 2 times
    in  HOTEL#CLEANLINESS 2 times
    in  HOTEL#GENERAL 1 times
    in  FOOD_DRINKS#QUALITY 1 times
"""
