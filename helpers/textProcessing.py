from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer, WordNetLemmatizer

from config import CACM_path


class TextProcessor:
    """
    Text processing of a given sentence.
    For a given sentence, TextProcessor will return the token and vocabulary lists,
    as well as the token frequency table.
    """

    def __init__(self, collection):
        # nltk.download('punkt')
        # nltk.download('wordnet')
        self.collection = collection
        self.tokenizer = RegexpTokenizer(r'\w+')
        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()
        self.tokens = []
        self.tokens_freq = {}
        self.vocabulary_full = []  # keep duplicates
        self.vocabulary = set()
        self.text = ""

    def process(self, text):
        self.text = text
        self.tokenize()
        self.lowercase()
        self.remove_stop_words()
        if self.collection != 'CACM':    # no need to lemmatize the CACM collection
            self.stem()
            # self.lemmatize()

        return self.tokens, self.vocabulary, self.tokens_freq

    def tokenize(self):
        self.tokens = self.tokenizer.tokenize(self.text)
        for token in self.tokens:
            if token in self.tokens_freq.keys():
                self.tokens_freq[token] += 1
            else:
                self.tokens_freq[token] = 1
        self.vocabulary = set(self.tokens)
        self.vocabulary_full = self.tokens

    def lowercase(self):
        self.vocabulary = set(token.lower() for token in self.vocabulary)
        self.vocabulary_full = [token.lower() for token in self.vocabulary_full]

    def remove_stop_words(self):
        with open(CACM_path + "/common_words") as f:
            stop_words = f.read()
        self.vocabulary = set(word for word in self.vocabulary if word not in stop_words)
        self.vocabulary_full = [word for word in self.vocabulary_full if word not in stop_words]

    def stem(self):
        self.vocabulary = set(self.stemmer.stem(word) for word in self.vocabulary)
        self.vocabulary_full = [self.stemmer.stem(word) for word in self.vocabulary_full]

    def lemmatize(self):
        self.vocabulary = set(self.lemmatizer.lemmatize(word) for word in self.vocabulary)
        self.vocabulary_full = [self.lemmatizer.lemmatize(word) for word in self.vocabulary_full]

    def get_vocabulary_full(self):
        return self.vocabulary_full


if __name__ == "__main__":
    processor = TextProcessor('CACM')
    sentence = 'A quick brown fox jumps over the lazy dog. fox dog'
    sentence2 = "At eight o'clock on Thursday morning Arthur didn't feel very good."
    print(processor.process(sentence))
    print(processor.get_vocabulary_full())
