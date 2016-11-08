from nltk.parse.stanford import StanfordDependencyParser

path_to_jar = '../scorenlp/stanford-corenlp-3.7.0.jar'
path_to_models_jar = '../scorenlp/stanford-corenlp-3.7.0-models.jar'
dependency_parser = StanfordDependencyParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)

corpus = "The food from the restaurant was very good but pricey which was the standard for everything in this hotel."
corpus = "The quick brown fox jumps over the lazy dog"
print(corpus)
result = dependency_parser.raw_parse(corpus)

for x in [parse.triples() for parse in result][0]:
	potential_adj = x[0]
	# if potential_adj[1] in ['JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS']:
	print(x[0], x[2])
	