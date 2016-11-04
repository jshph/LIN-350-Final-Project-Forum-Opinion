from bs4 import BeautifulSoup
import requests
import unicodedata

soup = BeautifulSoup(requests.get("http://www.head-fi.org/t/706595/review-ostry-kc06").text, \
		 "html.parser")

for x in soup.find_all('div', class_="wiki_markup"):
	reply_contents = []
	for p in x.find_all('p'):
		if p.string and p.string != u'\xa0':
			reply_contents.append(p.string.replace(u'\xa0', ' '))
	print(reply_contents)
	print()