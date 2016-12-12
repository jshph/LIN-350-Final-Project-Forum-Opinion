import re
from collections import defaultdict
import nltk
def grouped(iterable, n):
    "s -> (s0,s1,s2,...sn-1), (sn,sn+1,sn+2,...s2n-1), (s2n,s2n+1,s2n+2,...s3n-1), ..."
    return zip(*[iter(iterable)]*n)


with open('textrank_hotels_output.txt') as inf:
	inf.readline()
	inf.readline()

	invIndex = defaultdict(set)
	category_bins = defaultdict(set)

	for line in inf:
		if not line.strip():
			continue

		# is category title
		if "***" in line:
			catpat = re.compile('\w+') # re.compile('\w+#\w+')
			curCategory = catpat.findall(line)
			if curCategory:
			 	curCategory = curCategory[0]
			else:
				curCategory = ''
		else:
			keyphrasepat = re.compile('\w+')
			# get just the keywords. ignore the score.
			keyphrase = keyphrasepat.findall(line)[:-2]
			keyphrase_string = ' '.join(keyphrase)

			invIndex[keyphrase_string].add(curCategory)
			category_bins[curCategory].add(keyphrase_string)

	for key, el in invIndex.items():
		if '' in el:
			el.remove('')
		# print(key)
		# print('\t', el)


		if len(el) > 1:
			for cat in el:
				category_bins[cat].remove(key)
		del key

	# for cat, tokens in category_bins.items():
	# 	print(cat)
	# 	print('\t', len(list(tokens)))

	## Test against the original
	
	right = 0
	wrong = 0
	totalreviews = 0
	found = False

	with open('ABSA15_Hotels_parsed.txt') as testfile:
		for sentence, category in grouped(iter(testfile), 2):
			testcat = category.strip().split('#')[0].strip()
			testsentence = sentence.strip()

			if not testcat:
				continue

			for word in nltk.word_tokenize(testsentence):
				if word in invIndex:
					if testcat in invIndex[word]: # is this test category the one indexed category?
						right += 1
						found = True
						break
			if not found:
				wrong += 1

			totalreviews += 1
			found = False

	print("Accuracy: ", right / totalreviews)
	print("Wrong: ", wrong / totalreviews)

