## About this project

Final project made in LIN 350 at UT Austin, as an experiment in categorizing hotel reviews into the features they describe (i.e. room service, amenities, comfort). Employs Python NLTK (natural language processing) library and implements TextRank, an algorithm that extracts keywords from text in an unsupervised fashion.

Original motivations for this project were to categorize forum thread discussions around various products. We didn't pursue this because annotating our own dataset of forum threads was out of our scope, so we pivoted to hotel reviews instead (for which we had an annotated dataset). One major thing that we learned may help our future work with these kinds of data: forums feature more comparative experience, whereas product reviews are generally more standalone value judgments that are anecdotal, etc.

-------
## Notes to get started

store the below datasets in the root of this folder

http://snap.stanford.edu/data/amazon/productGraph/categoryFiles/reviews_Electronics_5.json.gz]

^^^ extracted and stored as `reviews_Electronics_amazon.json`

http://www.cs.cmu.edu/~jiweil/review.txt.zip

^^^ extracted and stored as `hotels_review_tripadvisor.txt`

-----
