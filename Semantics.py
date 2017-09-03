import nltk
from nltk.corpus import wordnet as wn

deer = wn.synset('deer.n.01')
elk = wn.synset('elk.n.01')
# #
# print(deer.path_similarity(elk))
# from nltk.corpus import wordnet_ic
# brown_ic = wordnet_ic.ic('ic-brown.dat')

# print(deer.lin_similarity(elk,brown_ic))
from nltk.collocations import *
# 'Amazon_Unlocked_Mobile.csv'
# '/Users/JamesFangmeyerJr/Desktop/dominican1.txt'

f = open('/Users/JamesFangmeyerJr/Desktop/dominican1.txt', 'r')
f.seek(0)
domdoc = f.read()
domtokens = nltk.wordpunct_tokenize(domdoc)

# print(domtokens[:100])
bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(domtokens)

# print(finder.nbest(bigram_measures.pmi, 10))
# print(finder.apply_freq_filter(2)) #Returns None -why?

## LDA
#pip install gensim
import gensim
from gensim import corpora, model_selection
dictionary = corpora.Dictionary(doc_set)
corpus = [dictionary.doc2bow(doc) for doc in doc_set]
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = 4,
id2word = dictionary, passes = 50)
print(ldamodel.print_topics(num_topics = 4, num_words = 5))
