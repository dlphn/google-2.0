from helpers import textProcessing
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s : %(message)s', level=logging.INFO)


class IndexBuilder:
    """
    Build the index for a given collection: tokens, vocabulary, tokens frequency.
    """

    def __init__(self, collection, data):
        self.collection = collection
        self.data = data
        self.processor = textProcessing.TextProcessor(collection)
        self.tokens = []
        self.tokens_freq = {}
        self.vocabulary = set()

    def build(self):
        result = self.processor.process(self.data)
        self.tokens = result[0]
        self. vocabulary = self.vocabulary.union(result[1])
        self.tokens_freq = result[2]
        # self.tokens_freq = sorted(self.tokens_freq.values(), reverse=True)

    def get_size(self):
        print("Tokens:", len(self.tokens))
        print("Vocabulary:", len(self.vocabulary))
        return len(self.tokens), len(self.vocabulary)

    def get_tokens(self):
        return self.tokens

    def get_vocabulary(self):
        return self.vocabulary

    def get_freq(self):
        return self.tokens_freq


