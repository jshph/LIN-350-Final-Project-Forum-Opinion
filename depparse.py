from bs4 import BeautifulSoup
from nltk.parse.stanford import StanfordDependencyParser
from nltk import RegexpParser
from nltk import pos_tag
import pickle
from collections import defaultdict

# traverse the tree t, in order to examine all the noun phrases.
# Count the nouns that occur in these noun phrases.
def traverse(t, nouns):
    try:
        t.label()
    except AttributeError:
        pass
    else:
        for child in t:
            traverse(child, nouns)
        if t.label() == "NP":
            for noun in filter(lambda x: x[1] == 'NN', t.leaves()):
                nouns[noun[0].strip('.(')] += 1



path_to_jar = '../scorenlp/stanford-corenlp-3.7.0.jar'
path_to_models_jar = '../scorenlp/stanford-corenlp-3.7.0-models.jar'
# dependency_parser = StanfordDependencyParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)

soup = BeautifulSoup(open("ABSA15_Hotels_Test.xml"), "lxml-xml")
corpus = list(soup.find_all('sentence'));
print(corpus)
sentences = [pos_tag(sent.contents[1].contents[0].split()) for sent in corpus]

topics = set(['room', 'food', 'internet', 'hotel', 'flight'])

np_grammar = RegexpParser('''
    NP: {<JJ>+<NN>}
    VBP_P: {<VBP|VBD>.*<JJ>}
    ''')

# initialize the nouns_histogram as a counter
nouns_histogram = defaultdict(int)

np_grammar = RegexpParser("NP: {(<JJ>* <NN.*>+ <IN>)? <JJ>* <NN.*>+}")
for sentence in sentences:
    result = np_grammar.parse(sentence)
    traverse(result, nouns_histogram)

# sort the nouns histogram by the highest count first, into a list
nouns_histogram_list = sorted(nouns_histogram.items(), reverse=True, key=lambda x: x[1])
for noun, count in nouns_histogram_list:
    print(noun, count)



# ideas:
# noun-phrase (regex) grammar extraction works well when we know the grammar.
# can we learn the grammar by observing many sentences that are tagged good/bad?
# extracting target topic words, then the surrounding sentence structure as the opinion.

# Attempted to parse entire tree for noun phrases. It's a bit difficult...

# def findNouns(sentence, tree, relevant_adjs_nouns):
#   trees = [parse.tree() for parse in sent_parse][0]:
#   for tree in trees:
#       children = tree.leaves()
#       if children[0] in topics:
#           return getAdjs(children)
#       else:

# def trav(tree, level):
#   # leaves = sum(list(tree.nodes[node_index]['deps'].values()), [])
#   for child in tree:
#       if not type(child) == str:
#           print(child.label())

# for idx, sentence in enumerate([sentences_list[3]]):
#   print(sentence)
#   trav(list(sentences_parsed)[idx].tree(), 0)