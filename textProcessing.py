from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer, WordNetLemmatizer


class TextProcessor:

    def __init__(self, collection):
        # nltk.download('punkt')
        # nltk.download('wordnet')
        self.collection = collection
        self.tokenizer = RegexpTokenizer(r'\w+')
        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()
        self.tokens = []
        self.text = ""

    def process(self, text):
        self.text = text
        self.tokenize()
        self.remove_stop_words()
        if self.collection != 'CACM':
            self.stem()
            # self.lemmatize()
        print(self.tokens, len(self.tokens))

    def tokenize(self):
        self.tokens = self.tokenizer.tokenize(self.text)
        # set all tokens to lowercase
        self.tokens = [token.lower() for token in self.tokens]

    def remove_stop_words(self):
        with open("CACM/common_words") as f:
            stop_words = f.read()
        self.tokens = [token for token in self.tokens if token not in stop_words]

    def stem(self):
        self.tokens = [self.stemmer.stem(token) for token in self.tokens]

    def lemmatize(self):
        self.tokens = [self.lemmatizer.lemmatize(token) for token in self.tokens]


if __name__ == "__main__":
    processor = TextProcessor('CACM')
    sentence = 'A quick brown fox jumps over the lazy dog.'
    processor.process(sentence)
