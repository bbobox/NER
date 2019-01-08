# -*- coding: utf-8 -*-
import sys, getopt

if len(sys.argv)<5:
  print('usage: main.py -i <inputfile> -o <outputfile>')
  sys.exit(2)

inputfile = ''
outputfile = ''
try:
  opts, args = getopt.getopt(sys.argv[1:],"i:o:",["ifile=","ofile="])
except getopt.GetoptError:
  print('usage: main.py -i <inputfile> -o <outputfile>')
  sys.exit(2)
for opt, arg in opts:
  if opt in ("-i", "--ifile"):
     inputfile = arg
  elif opt in ("-o", "--ofile"):
     outputfile = arg

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

def serialize_to_outfile(L,output_file_path):
    myDict=[]
    for i in range(len(L)):
        data ={"element":L[i][0],"frequency":int(L[i][1])}
        myDict.append(data)
    with open(output_file_path, 'w') as outfile:
        json.dump(myDict, outfile,indent=3,ensure_ascii=False)

def get_score(name_and_value):
   return name_and_value[1]

"----------------------------------------------------------------------"

file = open(inputfile, "r") #chemin du fichier
websites = getWebSiteSet(file)
cp = Corpus()
cp.set_content(websites)
L = sorted(cp.get_relevant_elements((1,3)), key=get_score, reverse=True)
serialize_to_outfile(L, outputfile+'.json')
