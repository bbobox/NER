# -*- coding: utf-8 -*-
import sys, getopt, distutils
from distutils.util import strtobool

inputfile = ''
outputfile = ''
mingram = 1
maxgram = 1
lemmatise = 1
remove_stopwords = 1
separator = '\n'
pattern = ""
try:
  opts, args = getopt.getopt(sys.argv[1:], "i:o:m:M:l:s:S:p:h", ["inputfile=", "outputfile=", "mingram=", "maxgram=", "lemmatise=", "stopwords=", "separator=", "pattern=", "help"])
except getopt.GetoptError:
  print('usage: main.py -i <inputfile> -o <outputfile> [-m <mingram>] [-M <maxgram>] [-l <lemmatise true|false>] [-s <stopwords treu|false>] [-S <separator>] [-p <pattern>]')
  sys.exit(2)
for opt, arg in opts:
  if opt in ("-i", "--inputfile"):
    inputfile = arg
  elif opt in ("-o", "--outputfile"):
    outputfile = arg
  elif opt in ("-m", "--mingram"):
    try:
      mingram = int(arg)
    except ValueError: print("-m parameter value is not an integer so it will take 1 !")
  elif opt in ("-M", "--maxgram"):
    try:
      maxgram = int(arg)
    except ValueError: print("-M parameter value is not an integer so it will take "+str(mingram)+" !")
  elif opt in ("-l", "--lemmatise"):
    try:
      lemmatise = distutils.util.strtobool(arg)
    except ValueError: print("-l parameter value is not a boolean like value so it will take 1 !")
  elif opt in ("-s", "--stopwords"):
    try:
      remove_stopwords = distutils.util.strtobool(arg)
    except ValueError: print("-s parameter value is not a boolean like value so it will take 1 !")
  elif opt in ("-S", "--separator"):
    separator = arg
  elif opt in ("-p", "--pattern"):
    pattern = arg
  elif opt in ("-h", "--help"):
    print('usage: main.py -i <inputfile> -o <outputfile> [-m <mingram>] [-M <maxgram>] [-l <lemmatise true|false>] [-s <stopwords treu|false>] [-S <separator>] [-p <pattern>]')
    print('-i    : input text file')
    print('-o    : output JSON file. No need to write .json, it will be added automatically')
    print('-m    : minimal n-gram. Default is 1')
    print('-M    : maximal n-gram. Default is minimal n-gram')
    print('-l    : if input text file must be lemmatized. Default is 1|true|yes|on. Can also be 0|false|no|off')
    print('-s    : remove stopwords from input text file. Default is 1|true|yes|on. Can also be 0|false|no|off')
    print('-S    : a string that represent the document separator. Default is \\n')
    print('-p    : a string that represent a pattern to work on in the input text file. Default is "" meaning no pattern search')
    sys.exit(0)

if inputfile=='' or outputfile=='':
  print('usage: main.py -i <inputfile> -o <outputfile> [-m <mingram>] [-M <maxgram>] [-l <lemmatise true|false>] [-s <stopwords treu|false>] [-S <separator>] [-p <pattern>]')
  sys.exit(2)

if mingram>maxgram: maxgram = mingram

from website import WebSite, Word, Dictionnary
#import treetaggerwrapper  # For proper print of sequences.
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

import json

def serialize_to_outfile(L, output_file_path):
    myDict = []
    for i in range(len(L)):
        data = {"element": L[i][0], "frequency": int(L[i][1])}
        myDict.append(data)
    with open(output_file_path, 'w') as outfile:
        json.dump(myDict, outfile, indent = 3, ensure_ascii = False)

def get_score(name_and_value):
   return name_and_value[1]

"----------------------------------------------------------------------"

file = open(inputfile, "r") #chemin du fichier
websites = getWebSiteSet(file, separator, pattern)
cp = Corpus()
cp.set_content(websites, lemmatise, remove_stopwords)
L = sorted(cp.get_relevant_elements((mingram, maxgram)), key = get_score, reverse = True)
serialize_to_outfile(L, outputfile+'.json')
