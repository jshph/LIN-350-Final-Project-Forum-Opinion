import re
from collections import defaultdict

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
			catpat = re.compile('\w+')
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
		print(key)
		print('\t', el)


		if len(el) > 2:
			for cat in el:
				category_bins[cat].remove(key)
		del key

	for cat, tokens in category_bins.items():
		print(cat)
		print('\t', list(tokens))

