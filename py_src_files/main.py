# -*- coding: utf-8 -*-
import sys
from parser import *

from corpus import Corpus
#from website import WebSite, Word, Dictionnary
#import treetaggerwrapper  # For proper print of sequences.
#import pprint
#from itertools import groupby

#import string
#import nltk
#from nltk.tokenize import RegexpTokenizer
#from nltk.corpus import stopwords
#import re

#import string
#import nltk
#from nltk.tokenize import RegexpTokenizer
#from nltk.corpus import stopwords
#import re
import sys

#from nltk.stem.snowball import FrenchStemmer


#from nltk import ngrams, FreqDist
#from nltk.tokenize import sent_tokenize, word_tokenize
#from nltk.stem import WordNetLemmatizer

"----------------------------------------------------------------------"

file = open("associations.txt", "r") #chemin du fichier
websites = getWebSiteSet(file)
cp = Corpus(websites)
print(cp.get_words_tfidf())
#Dic = createWordsDictionnary(websites)
#Dic.__str__()

#print(computeWordTF('www.anae.org', "événementiel", Dic, websites))


print()