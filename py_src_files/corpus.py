# -*- coding: utf-8 -*-
import nltk
nltk.download('stopwords')
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

import spacy
from spacy_lefff import LefffLemmatizer, POSTagger
nlp = spacy.load('fr')


def preprocess(sentence):

	#sentence = sentence.lower()
	tokenizer = RegexpTokenizer(r'\w+')
	tokens = tokenizer.tokenize(sentence)
	filtered_words = [w for w in tokens if not w in stopwords.words('french')]
	return  filtered_words #tokens #.join(filtered_words)

def lemmatise_sentence(sentence):
    """
    Re construit le texte/chaine de caractère avec le lemme de chaque chacun de son contenu
    :param sentence:
    :return:
    """
    res = ""
    doc = nlp(sentence)
    for i in doc:
        res = res +" " +i.lemma_
    return res



def remove_stops(sentence):
    """
    Re construit le texte/chaine de caractère avec les stops_words supprimés
    :param sentence:
    :return:
    """
    st = preprocess(sentence)
    res = ""
    for i in st:
        res = res + " "+i
    return res.lower()


class Corpus:

    def __init__(self):
        self.content = []
        self.list=[]
        self.websites_list=[]

    def set_content(self, websites, lemmatise, remove_stopwords):
        """
        Remplissage avec les contenus des elements web
        :param websites:
        """
        for i in websites:
            if websites[i].type!="": ws= websites[i].type.lower()
            else: ws= websites[i].desc.lower()
            if lemmatise: ws = lemmatise_sentence(ws)
            if remove_stopwords: ws = remove_stops(ws)
            if (ws!=""):
                self.content.append(ws)
                self.websites_list.append(websites[i].url)

    def get_indexed_elements(self, ngram_range=(1, 1)):
        """
        Recuperation de l'ensemble des elements indexés
        :param ngram_range: couple ( a,b) corespondant au element ngran indexés
        :return:
        """
        vectorizer = CountVectorizer(ngram_range = ngram_range)
        X = vectorizer.fit_transform(self.content)
        return vectorizer.get_feature_names()


    def get_words_frequencies(self, ngram_range=(1, 1)):
        """
        Calcul de la fréquences des elemnts ngram dans en fonction de chaque element du corpus
        :param ngram_range:
        :return:
        """
        count_vectorizer = CountVectorizer(ngram_range=ngram_range)
        X = count_vectorizer.fit_transform(self.content)
        return X.toarray()

    def get_words_tfidf(self, ngram_range=(1, 1)):
        """
        Calcul du tfidf des elemnts ngram dans en fonction de chaque elements du corpus
        :param ngram_range:
        :return:
        """
        tfidf_vectorizer = TfidfVectorizer(ngram_range=ngram_range)
        X = tfidf_vectorizer.fit_transform(self.content)
        return X.toarray()

    def get_relevant_elements(self, ngram_range=(1, 1)):
        """
        recpéruation des elements pertinants du corpus après le calcul du tf/idf
        :param ngram_range:
        :return: liste de couple(X,Y) avec X étant n-gram/words et Y la somme de ses fréquences
        """
        elements = self.get_indexed_elements(ngram_range=ngram_range)
        frequencies = self.get_words_frequencies(ngram_range=ngram_range)
        tfidf = self.get_words_tfidf(ngram_range=ngram_range)

        relevant = []
        relevant_words=[]
        n= len(tfidf)
        for doc in range(n):
            for element in range(len(elements)):
                if tfidf[doc][element] > 0:
                    if not (elements[element] in relevant_words):
                        relevant_words.append(elements[element])
                        total_frequency= self.compute_word_total_frequency(element, frequencies, self.content)
                        relevant.append((elements[element],total_frequency))

        return relevant

    def compute_word_total_frequency(self,word_id, frequency_Matrix, corpus):
        """

        :param word_id:
        :param frequency_Matrix:
        :param corpus:
        :return:
        """
        cpt = 0
        for i in range(len(corpus)):
            cpt += frequency_Matrix[i][word_id]
        return cpt



