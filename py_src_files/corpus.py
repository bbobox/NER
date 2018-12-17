#-*- coding: utf-8 -*-
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

def preprocess(sentence):
    # sentence = sentence.lower()
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(sentence)
    filtered_words = [w for w in tokens if not w in stopwords.words('french')]
    return filtered_words  # tokens #.join(filtered_words)

class Corpus:

    def __init__(self, websites):
        self.list = []
        self. words =[]

        for i in websites:
                ws = websites[i]
                desc = ws.desc
                self.list.append(desc)
                #print(preprocess(desc))



    def get_frequences_words(self,*ngram_range):
        if(ngram_range is not None):
            count_vectorizer = CountVectorizer(ngram_range=ngram_range)
        else:
            count_vectorizer = CountVectorizer()
        X = count_vectorizer.fit_transform(self.list)
        return X.toarray()


    def get_words_tfidf(self,*ngram_range):
        if (ngram_range is not None ):
            tfidf_vectorizer = TfidfVectorizer()
        else:
            tfidf_vectorizer = TfidfVectorizer(ngram_range=ngram_range)
        X = tfidf_vectorizer.fit_transform(self.list)
        return X.toarray()

