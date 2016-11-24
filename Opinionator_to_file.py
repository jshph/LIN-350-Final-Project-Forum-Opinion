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

sentenceList = []
# Fills dict
for curr_tag in tagList:
    sentence = ' '.join(curr_tag.contents[1].contents[0].split('\n'))
    sentenceTags = (sentence, [])
    for y in range(3, len(curr_tag) - 1):
        curCategory = curr_tag.contents[y].contents[1]['category']
        tags_dict[curCategory].append(sentence);
        sentenceTags[1].append(curCategory)
    sentenceList.append(sentenceTags)

# outputs sentences to file in the following format:
# sentence, line break, category(s), line break.
# To save time on BS import and XML parsing.
with open('ABSA15_Hotels_parsed.txt', 'w') as outf:
    for sentenceTag in sentenceList:
        outf.write(sentenceTag[0] +  '\n')
        for tag in sentenceTag[1]:
            outf.write(tag + " ")
        outf.write('\n')

# See contents of tag dictionary      
# print (tags_dict);

# used for binning up all categories for the adjectives they occur with
def rec_dd():
    return defaultdict(int)
adj_to_category = defaultdict(rec_dd)

# binning up all adjectives for the categories they occur with
# for key, review in tags_dict.items():
#     for rev in review:
#         rev_string = str(rev)
#         tokenizer = RegexpTokenizer(r'\w+')
#         tokenizer.tokenize(rev_string)
#         tokenized_review = word_tokenize(str(rev))
#         for i,j in nltk.pos_tag(tokenized_review):
#             if j in ['JJ', 'JJR', 'JJS']:
#                 # add other POS tags to list above
#                 token_dict[key].append(i)
#                 adj_to_category[i][key] += 