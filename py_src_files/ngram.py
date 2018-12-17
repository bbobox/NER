import re

sentence = "Natural-language processing (NLP) is an area of computer science " \
    "and artificial intelligence concerned with the interactions " \
    "between computers and human (natural) languages."


def get_tokens(s):
     # Convert to lowercases
    s = s.lower()
    
    # Replace all none alphanumeric characters with spaces
    s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)
    
    # Break sentence in the token, remove empty tokens
    tokens = [token for token in s.split(" ") if token != ""]
    n=len(tokens)

    return tokens
    

def generate_ngrams(s, n):
    tokens = get_tokens(s)

    # Use the zip function to help us generate n-grams
    # Concatentate the tokens into ngrams and return
    ngrams = zip(*[tokens[i:] for i in range(n)])
    
    return [" ".join(ngram) for ngram in ngrams]


def generate_ngrams_range(s,i_0, i_n ):
    ngrams=[]
    for i in range(i_0, i_n ):
        ngrams.append(generate_ngrams(s, i))

    return ngrams


#print(generate_ngrams_range(sentence,0,6))