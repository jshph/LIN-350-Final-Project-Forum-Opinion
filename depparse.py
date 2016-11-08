from bs4 import BeautifulSoup
from nltk.parse.stanford import StanfordDependencyParser
from nltk import RegexpParser
from nltk import pos_tag
import pickle

def traverse(t):
    try:
        t.label()
    except AttributeError:
        pass# print(t, end=" ")
    else:
        # Now we know that t.node is defined
        for child in t:
            traverse(child)
        if t.label() == "NP":
            print(t)



path_to_jar = '../scorenlp/stanford-corenlp-3.7.0.jar'
path_to_models_jar = '../scorenlp/stanford-corenlp-3.7.0-models.jar'
# dependency_parser = StanfordDependencyParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)

soup = BeautifulSoup(open("ABSA15_Hotels_Test.xml"), "lxml-xml")
corpus = list(soup.find_all('sentence'));
sentences = [pos_tag(sent.contents[1].contents[0].split()) for sent in corpus]

topics = set(['room', 'food', 'internet', 'hotel', 'flight'])

np_grammar = RegexpParser('''
    NP: {<JJ>+<NN>}
    VBP_P: {<VBP|VBD>.*<JJ>}
    ''')
np_grammar = RegexpParser("NP: {(<JJ>* <NN.*>+ <IN>)? <JJ>* <NN.*>+}")
for sentence in sentences:
    result = np_grammar.parse(sentence)
    traverse(result)


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