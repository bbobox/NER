import re

#from sklearn.feature_extraction.text import TfidfVectorizer

sentence = "Natural-language processing (NLP) is an area of computer science " \
    "and artificial intelligence concerned with the interactions " \
    "between computers and human (natural) languages."


def tok(s):
     # Convert to lowercases
    s = s.lower()
    
    # Replace all none alphanumeric characters with spaces
    s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)
    
    # Break sentence in the token, remove empty tokens
    tokens = [token for token in s.split(" ") if token != ""]
    n=len(tokens)

    return tokens
    

def generate_ngrams(s, n):
    tokens = tok(s)

    # Use the zip function to help us generate n-grams
    # Concatentate the tokens into ngrams and return
    ngrams = zip(*[tokens[i:] for i in range(n)])
    
    return [" ".join(ngram) for ngram in ngrams]



print(generate_ngrams(sentence, 4))    

#for i in range(0,len(tok(sentence))):
#               print(i)
#               print(generate_ngrams(sentence, i))



##-------------------------- tf/idf

def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(bow)
    for word, count in wordDict.items():
        tfDict[word] =  count/float(bowCount)
    return tdfDict


def computeIDF(docList):
    import math
    idfDict = {}
    N = len(docList)

    idfDict = dict.fromkeys(docList[0].keys(), 0)
    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                idfDict[word] +=1
                
    for word, val in idfDict.items():
        idfDict[word] = math.log10(N/ float(val))

    return idfDict

def computeTFIDF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.items():
        tfidf[word] = val*idfs[word]


#Calcul de TF
        
               
#print(computeIDF(sentence))
##" from nltk import ngram
##
##In [19]: %timeit x = list(find_ngrams(hamlet, 2))
##10 loops, best of 3: 147 ms per loop
##
##In [20]: %timeit x = list(ngrams(hamlet, 2))
##10 loops, best of 3: 82.7 ms per loop"
