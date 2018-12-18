# -*- coding: utf-8 -*-
from website import WebSite, Word, Dictionnary
import treetaggerwrapper  # For proper print of sequences.
import pprint
from itertools import groupby

import string
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import re

import string
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import re
import sys

from nltk.stem.snowball import FrenchStemmer

from corpus import *

from parser import *

from nltk import ngrams, FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer

"----------------------------------------------------------------------"

file = open("../asso_parsed.out", "r") #chemin du fichier
websites = getWebSiteSet(file)
cp = Corpus()
cp.set_content(websites)
print(cp.get_relevant_elements())
