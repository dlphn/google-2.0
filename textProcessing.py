import nltk
from nltk.tokenize import RegexpTokenizer


class TextProcessor:

    def __init__(self):
        nltk.download('punkt')
        self.tokenizer = RegexpTokenizer(r'\w+')
        self.tokens = []

    def tokenize(self, text):
        self.tokens = self.tokenizer.tokenize(text)
        print(self.tokens)


if __name__ == "__main__":
    processor = TextProcessor()
    sentence = 'Eighty-seven miles to go, yet.  Onward!'
    processor.tokenize(sentence)
