import os
import logging
import time
from helpers import indexBuilder

logging.basicConfig(format='%(asctime)s - %(levelname)s : %(message)s', level=logging.INFO)


class CS276Index:
    """
    Build the CS276 collection's index:
    - parse the different files in the multiple folders
    - build index
    """

    def __init__(self, repo_id=-1):
        self.index = None
        self.repo_id = repo_id
        self.document_dict = {}

    def build(self, half=False):
        """
        Build the index and the document dictionary (documentID, document)
        """
        # logging.info("Start building index...")
        start = time.time()
        data = ""
        if self.repo_id < 0 or self.repo_id > 10:  # build on the whole collection
            for file_id in range(10):
                count = 0
                for filename in os.listdir("pa1-data/" + str(file_id)):
                    with open("pa1-data/" + str(file_id) + "/" + filename) as f:
                        read_data = f.read()
                        data = data + read_data
                        self.document_dict[str(file_id) + "-" + str(count)] = read_data
                        count += 1
                logging.info("Read {0}/10 folders".format(file_id + 1))
        # else:  # build for one repository
        #     count = 0
        #     for filename in os.listdir("pa1-data/" + str(self.repo_id)):
        #         with open("pa1-data/" + str(self.repo_id) + "/" + filename) as f:
        #             read_data = f.read()
        #             data = data + read_data
        #             self.document_dict[str(self.repo_id) + "-" + str(count)] = read_data
        #             count += 1
        #     logging.info("Read folder pa1-data/{0}/".format(self.repo_id))
        if half:
            data = data[:len(data)//2]
        self.index = indexBuilder.IndexBuilder('CS276', data)
        self.index.build()
        end = time.time()
        # logging.info("Index built in {0} seconds".format(end - start))
        self.index.get_size()

    def get_tokens(self):
        print(self.index.get_tokens())

    def get_vocabulary(self):
        print(self.index.get_vocabulary())

    def get_size(self):
        self.index.get_size()

    def get_freq(self):
        return self.index.get_freq()

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

    def get_document_dict(self, repo_id=-1):
        if repo_id >= 0 or repo_id <= 10:
            return {k: v for k, v in self.document_dict.items() if k.startswith(str(repo_id) + '-')}
        return self.document_dict


if __name__ == "__main__":
    '''Run to calculate number of tokens, vocabulary
    Uncomment parts to see the graph ar calculate values for half of the text
    '''
    index = CS276Index()
    index.build()
    # index.get_tokens()

    # index.get_size()

    # Uncomment here to see values for half of the text
    # print()
    # print("For half of the text:")  # Tokens: 12758945 - Vocabulary: 8432796
    # index.build(half=True)

    # Uncomment here to see the frequency graph
    # graph = FrequencyRankGraph(index.get_freq())
    # graph.draw_graph()
    # graph.draw_log_graph()





