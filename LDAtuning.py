import gensim
import sys
import hw2module as LDA

sentences_tagged = []
with open('ABSA15_Hotels_parsed.txt') as inf:
	while True:

		sentence_raw = inf.readline()
		if not sentence_raw: break
		category_raw = inf.readline()
		if category_raw == "\n":
			category_raw = None # indicates that no category was assigned.
		sentences_tagged.append((sentence_raw, category_raw))

# list of all sentences that have assigned categories. These sentences are 
# converted into lists, split by whitespace.
split_sentences_raw = [x[0].split() for x in sentences_tagged if x[1] is not None]

# run preprocess(), which takes a list of words (sentence) and removes
# all punctuation and stopwords from each word, returning the same structure.
preprocessed_sentences_raw = [LDA.preprocess(s) for s in split_sentences_raw]

# create a gensim dictionary, save it to file
gdict = LDA.saveInitialDictionary(preprocessed_sentences_raw)

# experiment with number of topics
LDA.make_and_show_lda_model(preprocessed_sentences_raw, gdict, 10, show_docs = True)