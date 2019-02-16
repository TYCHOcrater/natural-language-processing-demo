
import nltk
arpabet = nltk.corpus.cmudict.dict()
for word in ('barbels', 'barbeque', 'barbequed', 'barbequeing', 'barbeques'):
    print(arpabet[word])
