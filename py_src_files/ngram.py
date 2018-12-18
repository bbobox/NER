import re

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
    

def generate_ngram(s, n):
    tokens = tok(s)

    # Use the zip function to help us generate n-grams
    # Concatentate the tokens into ngrams and return
    ngrams = zip(*[tokens[i:] for i in range(n)])
    
    return [" ".join(ngram) for ngram in ngrams]



def ngrams_range(s, l_b,u_p):
    ngrans= []
    for i in range(l_b,u_p):
        ngrans.append(generate_ngram(s, i))
    return ngrans


print(generate_ngram(sentence, 4))