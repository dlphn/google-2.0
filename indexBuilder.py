import textProcessing


class IndexBuilder:

    def __init__(self, collection, data):
        self.collection = collection
        self.data = data
        self.processor = textProcessing.TextProcessor(collection)
        self.tokens = []
        self.tokens_freq = {}
        self.vocabulary = []

    def build(self):
        if self.collection == 'CACM':
            for line in self.data:
                sentence = self.data[line]
                result = self.processor.process(sentence)
                self.tokens += result[0]
                self.tokens_freq = {key: self.tokens_freq.get(key, 0) + result[2].get(key, 0) for key in set(self.tokens_freq) | set(result[2])}
                for word in result[1]:
                    if word not in self.vocabulary:
                        self.vocabulary.append(word)
        else:
            result = self.processor.process(self.data)
            self.tokens = result[0]
            self.vocabulary = result[1]
            self.tokens_freq = result[2]
            # self.tokens_freq = sorted(self.tokens_freq.values(), reverse=True)

    def get_size(self):
        print("Tokens:", len(self.tokens))
        print("Vocabulary:", len(self.vocabulary))

    def get_tokens(self):
        return self.tokens

    def get_vocabulary(self):
        return self.vocabulary

    def get_freq(self):
        return self.tokens_freq


if __name__ == "__main__":
    indexCACM = IndexBuilder('CACM', {
        '2': "The white fox A quick brown fox jumps over the lazy dog. fox, brown, quick",
        '3': "Arthur and the kettle At eight o'clock on Thursday morning Arthur didn't feel very good. sick, work",
    })
    index = IndexBuilder('CS276', "A quick brown fox jumps over the lazy fox. At eight o'clock on Thursday morning Arthur didn't feel very good.")
    index.build()
    index.get_size()
    print(index.get_freq())
