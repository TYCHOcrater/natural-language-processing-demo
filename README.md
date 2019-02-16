## nlp-demo

https://en.wikipedia.org/wiki/Natural_language_processing



use following code to install nltk:

```
sudo pip install -U nltk
```
install numpy:

```
sudo pip install -U numpy
```
than you need to install scikit-learn
```
pip install -U scikit-learn
```

## links

+ [cluster analysis](https://en.wikipedia.org/wiki/Cluster_analysis)
+ [nltk](https://www.nltk.org)
+ [lexical analysis](https://en.wikipedia.org/wiki/Lexical_analysis)
  + [tokenization](https://en.wikipedia.org/wiki/Lexical_analysis#Tokenization)
  
```import VideoFileClip``` to load a video, TextClip to overlay text, and CompositeVideoClip to take
two or more clips and overlay them as layers

```def compose``` takes a text and duration. duration is optional and defaults to 4.0

```print(sentence,"is",cl.classify(sentence))``` classify a sentence
get the probability 
```prob = cl.prob_classify("I don't like tings")```
```print("The probability that this sentence is negative is", prob.prob("neg"))```
```print("The probability that this sentence is positive is", prob.prob("pos"))```

analyze a text
```text = open("pride.txt").read()```
```blob = TextBlob(text)```


