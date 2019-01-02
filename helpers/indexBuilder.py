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
        self.vocabulary = []

    def build(self):
        if self.collection == 'CACM':
            for line in self.data:
                sentence = self.data[line]
                result = self.processor.process(sentence)
                self.tokens += result[0]
                # self.tokens_freq += result[2]
                for word in result[1]:
                    if word not in self.vocabulary:
                        self.vocabulary.append(word)
        else:
            result = self.processor.process(self.data)
            self.tokens = result[0]
            vocab_size = len(result[1])
            print(vocab_size)
            count = 0
            for word in result[1]:
                if word not in self.vocabulary:
                    self.vocabulary.append(word)
                count += 1
                if count % 1000 == 0:
                    logging.info("Processed {0}/{1}".format(count, vocab_size))
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
    indexCACM.build()
    indexCACM.get_size()
    print(indexCACM.get_vocabulary())
    print(indexCACM.get_freq())
    index = IndexBuilder('CS276', "A quick brown fox jumps over the lazy fox. At eight o'clock on Thursday morning Arthur didn't feel very good. But the fox was happy to see Arthur.")
    index.build()
    index.get_size()
    print(index.get_vocabulary())
    print(index.get_freq())
