import nltk

nltk.download('punkt')

sentence = """At eight o'clock on Thursday morning"""

tokens = nltk.word_tokenize(sentence)

print(tokens)