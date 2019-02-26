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
        # logging.info("Start building index...")
        start = time.time()
        data = self.get_document_dict(half)
        all_words = " ".join(data.values())
        self.index = indexBuilder.IndexBuilder('CACM', all_words)
        self.index.build()
        end = time.time()
        # logging.info("Index built in {0} seconds".format(end - start))

    def get_tokens(self):
        print(self.index.get_tokens())

    def get_vocabulary(self):
        print(self.index.get_vocabulary())

    def get_size(self):
        self.index.get_size()

    def get_term_dict(self):
        """
        Build the term dictionary (term, termID)
        :return: terms dictionary
        """
        dict_term = dict()
        term_id = 1
        for vocab in sorted(list(self.index.get_vocabulary())):
            dict_term[vocab] = term_id
            term_id += 1
        return dict_term

    def get_document_dict(self, id=-1, half=False):
        """
        Build the document dictionary (documentID, document)
        :param id: int
        :param half: bool
        :return: document dictionary
        """
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
    '''Run to calculate number of tokens, vocabulary
    Uncomment parts to see the graph ar calculate values for half of the text
    '''
    index = CACMIndex()
    index.build()
    index.get_size()

    # Uncomment here to see values for half of the text
    # print()
    # print("For half of the text:")
    # index.build(half=True)
    # index.get_size()

    # Uncomment here to see the frequency graph
    # graph = FrequencyRankGraph(index.get_freq())
    # graph.draw_graph()
    # graph.draw_log_graph()
