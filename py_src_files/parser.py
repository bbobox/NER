# -*- coding: utf-8 -*-
from website import WebSite, Word, Dictionnary
import treetaggerwrapper  # For proper print of sequences.
import pprint
from itertools import groupby

from nltk import ngrams, FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer

import re # regex library importation

import string
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

import sys

import argparse


#tagger = treetaggerwrapper.TreeTagger(TAGLANG='fr')

#f = open('workfile', 'w')

def getWebSiteSet(file):
    """
    retourne l'ensemble des Objects de type WebSites selon le fichier parsé 
    """
    i=0
    tour=0
    title=""
    ws=""
    des=""
    websites = {}
    for ligne in file:
        if((ligne!="\n" or tour!=0)):
            i=i+1
            if(i%3==1):
                title = ligne
                tour = tour+1
            else:
                if(i%3==2):
                    ws = ligne.split("\n")[0]
                    tour = tour+1
                else:
                    if(i%3)==0:
                        des = ligne
                        websites[ws]=WebSite(ws,des,title)
                        tour = 0
    return websites


def computeWordTF(url, wordText, dictionnary,websites):
    wordInf = dictionnary.recupInfoMot(wordText)
    if wordInf !=None:
        if url in wordInf.listDoc:
            n = wordInf.listDoc[url]["occ"]
            p= websites[url].nwords
            return n/float(p)
    else:
        return None



def preprocess(sentence):
	#sentence = sentence.lower()
	tokenizer = RegexpTokenizer(r'\w+')
	tokens = tokenizer.tokenize(sentence)
	filtered_words = [w for w in tokens if not w in stopwords.words('french')]
	return  filtered_words #tokens #.join(filtered_words)


def createWordsDictionnary(websites):
    """
    Creation du dictionnaire
    """
    Dic = Dictionnary()
    for i in websites:
        #test= ""
        ws = websites[i]
        desc = ws.desc
        words= preprocess(desc)
        tags= tagger.tag_text(desc)
        wordTagged = treetaggerwrapper.make_tags(tags)
        words =[]
        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(desc)
        for word in wordTagged:
            
            try:
                getattr(word, 'lemma')        
            except AttributeError:
               print()
               #print(word)
            else:
                if(word.word in tokens):
                    words.append(word.lemma)
        #ws.wordsNumber(len(words))
        filtered_words = [w for w in words if not w in stopwords.words('french')]
        ws.wordsNumber(len(filtered_words))
        fdist = FreqDist(filtered_words)
        for j in fdist:
            A = Word(j)
            A.linkToText(ws.url, fdist[j])
            Dic.majMotArbre(A)
    return Dic


#file = open("/home/boka/Bureau/projet_annuel/associations.txt", "r") #chemin du fichier
#Dic = createWordsDictionnary(getWebSiteSet(file))
#Dic.__str__()

#computeWordTF('www.anae.org', "événementiel", Dic)
