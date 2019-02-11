from textblob import TextBlob
from textblob.classifiers import NaibeBayesClassifier

train = [
    ('i am happy today', 'pos'),
    ('this is a good burger', 'pos'),
    ('you\'re a good boy', 'pos'),
    ('you are doing well', 'pos'),

    ('i do not like you', 'neg'),
    ('do not go there', 'neg'),
    ('this is so frustrating', 'neg'),
    ('things are bad', 'neg')
]

cl = NaiveBayesClassifier(train)

sentence = "I feel really bad"

print(sentence, "is", cl.classify(sentence))

prob = cl.prob_classify("I don't like things")
print("The probability that this sentence is negative is", prob.prob("neg"))
print("The probability that this sentence is positive is", prob.prob("pos"))

text = open("pride.txt").read()

blob = TextBlob(text)
results = {
        "pos": [],
        "neg": []
}

for sentence in blob.sentences:
    cat  = cl.classify(sentence)
    results[cat].append(sentence)

print("There are", len(results["pos"]), "positive sentences and", len(results["neg"]), "negative sentences.")
