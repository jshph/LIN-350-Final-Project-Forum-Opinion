from nltk import sem
import nltk
import re

f = open('headphonereview.txt')
sentences = nltk.sent_tokenize(f.read())
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]

SOUND = re.compile(r'.*\bsound(s)?\b.*')

for i, sent in enumerate(tagged_sentences):
	sent = nltk.ne_chunk(sent)
	rels = sem.extract_rels('NE', 'NE', sent, corpus='ace', pattern=SOUND)
	for rel in rels:
		print(sem.rtuple(rel))