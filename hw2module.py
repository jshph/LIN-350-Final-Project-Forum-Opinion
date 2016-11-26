# Joshua's HW2, used as a module for LDA in final project

# Utility functions for all tasks

import string
import gensim
from collections import defaultdict
import os
translator = str.maketrans({key: None for key in string.punctuation})

isInitialDictionaryDone = True

def preprocess(doc):
	stopword_filename = "./stopwords-augmented.txt"
	f = open(stopword_filename)
	stopwords = set(f.read().split())
	f.close()
	stopwords.add('--')
	stopwords.add('``')
	stopwords.add("''")
	for punct in string.punctuation:
		stopwords.add(punct)
	
	context_window_list = []
	for idx, word in enumerate(doc[:-2]):
		# strip punctuation and lowercase words.
		context_window = ' '.join([w.lower().translate(translator) for w in doc[idx:idx + 3]])
		context_window_list.append(context_window)
	print(context_window_list)
	return context_window_list
	# return [w.lower().translate(translator) for w in doc if w.lower() not in stopwords]

# Original function taken from website with some additional functionality:
# - gathers information on the top topics by using a Counter that is initialized in the caller.
# - Also passes topic words to a structure that is defined in the caller.
def make_and_show_lda_model(texts, gdict, numtopics, show_docs = True):
	# represent the corpus in sparse matrix format, bag-of-words
	corpus = [gdict.doc2bow(text) for text in texts]
	# now we make an LDA object.
	# in case we have a larger text collection (such as the Brown corpus),
	# make sure to set "passes" to a reasonably high number in order not to have all topics
	# come out equal. 20 seems to work.
	lda_obj = gensim.models.ldamodel.LdaModel( \
		corpus, id2word=gdict, num_topics=numtopics, passes = 20)

	# how do our texts look: how important is each topic there?
	if show_docs:
		print("Showing how important each topic is for each document")
		lda_corpus = lda_obj[corpus]
		for docindex, doc in enumerate(lda_corpus):
			print( "Chunk excerpt ", docindex, ":", end = " ")
			for word in texts[docindex][:20]: print( word, end = " ")
			print("\n")
			for topic, weight in doc:
				topic_words = [x[0] for x in sorted(lda_obj.show_topic(topic), key=lambda x : x[1])]
				print( "Topic", topic,", which has keywords: ", topic_words, \
					"\nWith weight of", round(weight, 2))
			print("\n")

	# returns which topics were most frequently shown. Used for final printing of
	# most frequent documents.

def saveInitialDictionary(originals_words):
	gdict = gensim.corpora.Dictionary(originals_words)
	gdict.save('./gdict_originals_words.dict')
	return gdict

# gdict = gensim.corpora.Dictionary.load('./gdict_originals_words.dict')

#### Example code: from task one in HW2
"""
gdict = saveInitialDictionary((itertools.chain.from_iterable(originals_words.values())))
for sotu in originals_words.values():
	make_and_show_lda_model(sotu, gdict, 25, show_docs = True)
"""