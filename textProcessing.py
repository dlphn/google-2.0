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
        self.tokens_freq = {}
        self.vocabulary = []
        self.text = ""

    def process(self, text):
        self.text = text
        self.tokenize()
        self.lowercase()
        self.remove_stop_words()
        if self.collection != 'CACM':
            self.stem()
            # self.lemmatize()

        # print(self.tokens, len(self.tokens))
        # print(self.vocabulary, len(self.vocabulary))
        return self.tokens, self.vocabulary, self.tokens_freq

    def tokenize(self):
        self.tokens = self.tokenizer.tokenize(self.text)
        for token in self.tokens:
            if token in self.tokens_freq.keys():
                self.tokens_freq[token] += 1
            else:
                self.tokens_freq[token] = 1
        self.vocabulary = self.tokens

    def lowercase(self):
        self.vocabulary = [token.lower() for token in self.vocabulary]

    def remove_stop_words(self):
        with open("CACM/common_words") as f:
            stop_words = f.read()
        self.vocabulary = [word for word in self.vocabulary if word not in stop_words]

    def stem(self):
        self.vocabulary = [self.stemmer.stem(word) for word in self.vocabulary]

    def lemmatize(self):
        self.vocabulary = [self.lemmatizer.lemmatize(word) for word in self.vocabulary]


if __name__ == "__main__":
    processor = TextProcessor('CACM')
    sentence = 'A quick brown fox jumps over the lazy dog.'
    sentence2 = "At eight o'clock on Thursday morning Arthur didn't feel very good."
    processor.process(sentence2)
