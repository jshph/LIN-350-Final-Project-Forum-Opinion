# Parse the JSON TripAdvisor dataset, which has more metadata
# than we need. We need just the review text, split up into tokenized sentences,
# to train our gensim model. The gensim dict will contain topics extracted from
# this corpus.

# IMPORTS AND CONSTANTS

import json

from nltk.tokenize import RegexpTokenizer
import nltk.data
# tokenizer used for splitting text into sentences
sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
# tokenizer used for splitting sentences into words
word_tokenizer = RegexpTokenizer(r'\w+')

from nltk.corpus import stopwords
STOPS = set(stopwords.words('english'));


TEXTRANK = True

# Parse the JSON
sentences = []
reviews = []
# with open('hotel_review_tripadvisor.txt') as taJSON:
with open('reviews_Electronics_amazon.json') as elJSON:
	reviewNo = 0
	while reviewNo < 800:
		# jsonReview = json.loads(taJSON.readline())['text']
		jsonReview = json.loads(elJSON.readline())['reviewText']
		if not TEXTRANK:
			review = sentence_tokenizer.tokenize(jsonReview)
			for sentence in review:
				sentence_tokenized = word_tokenizer.tokenize(sentence)
				sentences.append(sentence_tokenized)
		else:
			reviews.append(jsonReview)
		reviewNo += 1


"""
Notes on using Gensim:
- reviews are already pretty short. Stripping stopwords can reduce sentences to too
short a corpus to discern (and train) the topic. That's why many generated topics
are not making sense.
- ideally, a corpus (sentence or more) should contain several words.
"""

if not TEXTRANK:

	import gensim
	import hw2module as LDA

	# run preprocess(), which takes a list of words (sentence) and removes
	# all punctuation and stopwords from each word, returning the same structure.
	preprocessed_sentences_raw = [LDA.preprocess(s) for s in sentences]

	# create a gensim dictionary, save it to file
	gdict = LDA.saveInitialDictionary(preprocessed_sentences_raw)

	# experiment with number of topics
	LDA.make_and_show_lda_model(sentences, gdict, 15, show_docs = True)

else:

	import TextRank as tr

	for review in reviews:
		for scoring in tr.score_keyphrases_by_textrank(review):
			print(scoring)
		print()