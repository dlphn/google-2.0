import os
import logging
import time
from helpers import indexBuilder

logging.basicConfig(format='%(asctime)s - %(levelname)s : %(message)s', level=logging.INFO)

from frequencyRankGraph import *



class CS276Index:
    """
    Build the CS276 collection's index:
    - parse the different files in the multiple folders
    - build index
    """

    def __init__(self):
        self.index = None

    def build(self, half=False):
        logging.info("Start building index...")
        start = time.time()
        data = ""
        for file_id in range(10):
            for filename in os.listdir("pa1-data/" + str(file_id)):
                with open("pa1-data/" + str(file_id) + "/" + filename) as f:
                    read_data = f.read()
                    data = data + read_data
            logging.info("Read {0}/10 folders".format(file_id + 1))
        if half:
            data = data[:len(data)//2]
        self.index = indexBuilder.IndexBuilder('CS276', data)
        self.index.build()
        end = time.time()
        logging.info("Index built in {0} seconds".format(end - start))
        self.index.get_size()

    def get_tokens(self):
        print(self.index.get_tokens())

    def get_vocabulary(self):
        print(self.index.get_vocabulary())

    def get_freq(self):
        return self.index.get_freq()


if __name__ == "__main__":
    index = CS276Index()
    index.build()
    # index.get_tokens()
    # index.get_vocabulary()

    # print()
    # print("For half of the text:")  # Tokens: 12758945 - Vocabulary: 8432796
    # index.build(half=True)

    graph = FrequencyRankGraph(index.get_freq())
    graph.draw_graph()
    graph.draw_log_graph()





