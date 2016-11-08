from bs4 import BeautifulSoup
import requests
import unicodedata
import lxml
import re
import string

# Creates soup
soup = BeautifulSoup(open("ABSA15_Hotels_Test.xml"), "lxml-xml")


# Creates the dictionary holding tags/list of responses about said tags
tags_dict = dict();

# Gets all opinion tags
opinion = soup.find_all('Opinion')

# Makes a key for each category and sets its value as an empty array
for curropinion in opinion:  
    tags_dict[curropinion['category']] = [];


# Gets all sentence tags (includes contents)
tagList = soup.find_all('sentence');

# Fills dict
for x in range(0, len(tagList)):
    curr_tag = tagList[x];
    sentence = curr_tag.contents[1].contents
    for y in range(3, len(curr_tag) - 1):
        tags_dict[curr_tag.contents[y].contents[1]['category']].append(sentence);

# See contents of dictionary      
print (tags_dict);
        
