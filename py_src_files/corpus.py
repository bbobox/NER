# -*- coding: utf-8 -*-
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer


def preprocess(sentence):
	#sentence = sentence.lower()
	tokenizer = RegexpTokenizer(r'\w+')
	tokens = tokenizer.tokenize(sentence)
	filtered_words = [w for w in tokens if not w in stopwords.words('french')]
	return  filtered_words #tokens #.join(filtered_words)

class Corpus:

    def __init__(self):
        self.content = []
        self.list=[]

    def set_content(self,websites):
        """
        Remplissage avec les contenus des elements web
        :param websites:
        """
        for i in websites:
            ws = websites[i].desc
            self.content.append(ws)

    def get_indexed_elements(self, ngram_range=(1,1)):
        """
        Recuperation de l'ensemble des elements indexés
        :param ngram_range: couple ( a,b) corespondant au element ngran indexés
        :return:
        """
        vectorizer = CountVectorizer(ngram_range=ngram_range)
        X = vectorizer.fit_transform(self.content)
        return vectorizer.get_feature_names()


    def get_words_frequencies(self, ngram_range=(1,1)):
        """
        Calcul de la fréquences des elemnts ngram dans en fonction de chaque element du corpus
        :param ngram_range:
        :return:
        """
        count_vectorizer = CountVectorizer(ngram_range=ngram_range)
        X = count_vectorizer.fit_transform(self.content)
        return X.toarray()

    def get_words_tfidf(self, ngram_range=(1,1)):
        """
        Calcul du tfidf des elemnts ngram dans en fonction de chaque elements du corpus
        :param ngram_range:
        :return:
        """
        tfidf_vectorizer = TfidfVectorizer(ngram_range=ngram_range)
        X = tfidf_vectorizer.fit_transform(self.content)
        return X.toarray()





