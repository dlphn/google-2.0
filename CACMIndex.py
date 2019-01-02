import logging
import time

from config import CACM_path
from helpers import indexBuilder, CACMParser

logging.basicConfig(format='%(asctime)s - %(levelname)s : %(message)s', level=logging.INFO)

from frequencyRankGraph import *


class CACMIndex:
    """
    Build the CACM collection's index:
    - parse the cacm.all file
    - build index
    """

    def __init__(self):
        self.parser = CACMParser.CACMParser()
        self.index = None

    def build(self, half=False):
        logging.info("Start building index...")
        start = time.time()
        data = self.get_documentID(half)
        all_words = " ".join(data.values())
        self.index = indexBuilder.IndexBuilder('CACM', all_words)
        self.index.build()
        end = time.time()
        logging.info("Index built in {0} seconds".format(end - start))
        self.index.get_size()

    def get_tokens(self):
        print(self.index.get_tokens())

    def get_vocabulary(self):
        print(self.index.get_vocabulary())

    def get_termID(self):
        termID = dict()
        id = 1
        for voca in self.index.get_vocabulary():
            termID[id] = voca
            id += 1
        return termID

    def get_documentID(self, half=False):
        with open(CACM_path + "/cacm.all") as f:
            read_data = f.read()
        if half:
            read_data = read_data[:len(read_data)//2]
        dic = self.parser.parse_documents(read_data)
        data = self.parser.parse_all(dic)
        return data

    def get_freq(self):
        return self.index.get_freq()



if __name__ == "__main__":
    index = CACMIndex()
    index.build()
    # index.get_tokens()
    # index.get_vocabulary()
    # print(index.get_termID())
    # print(index.get_documentID())

    # print()
    # print("For half of the text:")
    # index.build(half=True)

    graph = FrequencyRankGraph(index.get_freq())
    graph.draw_graph()
    graph.draw_log_graph()
