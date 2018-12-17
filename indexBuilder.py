# from textProcessing import *
import textProcessing
import CACMParser


class IndexBuilder:

    def __init__(self, collection, data):
        self.data = data
        self.processor = textProcessing.TextProcessor(collection)
        self.tokens = []
        self.vocabulary = []

    def build(self):
        for line in self.data:
            sentence = self.data[line]
            result = self.processor.process(sentence)
            self.tokens += result[0]
            for word in result[1]:
                if word not in self.vocabulary:
                    self.vocabulary.append(word)

    def get_size(self):
        print("Tokens:", len(self.tokens))
        print("Vocabulary:", len(self.vocabulary))

    def get_tokens(self):
        return self.tokens

    def get_vocabulary(self):
        return self.vocabulary


if __name__ == "__main__":
    index = IndexBuilder('CACM', {
        '2': "The white fox A quick brown fox jumps over the lazy dog. fox, brown, quick",
        '3': "Arthur and the kettle At eight o'clock on Thursday morning Arthur didn't feel very good. sick, work",
    })
    index.build()
    index.get_size()
