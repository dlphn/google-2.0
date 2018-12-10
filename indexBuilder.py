from textProcessing import *


class IndexBuilder:

    def __init__(self, data):
        self.data = data
        self.processor = TextProcessor('CACM')
        self.tokens = []
        self.vocabulary = []


if __name__ == "__main__":
    index = IndexBuilder({
        '2': "A quick brown fox jumps over the lazy dog.",
        '3': "At eight o'clock on Thursday morning Arthur didn't feel very good."})
