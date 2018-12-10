import nltk
from nltk.tokenize import RegexpTokenizer


class TextProcessor:

    def __init__(self):
        # nltk.download('punkt')
        self.tokenizer = RegexpTokenizer(r'\w+')
        self.tokens = []
        self.text = ""

    def process(self, text):
        self.text = text
        self.tokenize()
        self.remove_stop_words()
        print(self.tokens, len(self.tokens))

    def tokenize(self):
        self.tokens = self.tokenizer.tokenize(self.text)
        # set all tokens to lowercase
        self.tokens = [token.lower() for token in self.tokens]

    def remove_stop_words(self):
        with open("CACM/common_words") as f:
            stop_words = f.read()
        self.tokens = [token for token in self.tokens if token not in stop_words]


if __name__ == "__main__":
    processor = TextProcessor()
    sentence = 'Eighty-seven miles to go, yet.  Onward!'
    processor.process(sentence)
