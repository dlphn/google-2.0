import logging
import json
from collections import defaultdict
from itertools import groupby
from CACMIndex import CACMIndex
from CS276Index import CS276Index
from config import index_path

from BSBIndex import BSBIndex

logging.basicConfig(format='%(asctime)s - %(levelname)s : %(message)s', level=logging.INFO)


def get_key(item):
    return item[0]


class BSBI:
    """
    Build a Block Sort-based index
    """

    def __init__(self, collection):
        self.collection = collection
        self.blocks = []
        self.intermediate_results = []
        self.index = {}
        self.terms = {}
        self.documents = {}

    def build(self):
        self.segment()
        self.build_inverted_index()
        self.merge()
        self.write("index", self.index)
        self.write("documents", self.documents)
        self.write("terms", self.terms)
        logging.info("Finished building inverted index.")

    def segment(self):
        """
        Segment collection in blocks
        """
        if self.collection == 'CACM':
            collection_index = CACMIndex()
            collection_index.build()
            self.blocks.append(collection_index)
        elif self.collection == 'CS276':
            collection_index = CS276Index()
            collection_index.build()
            self.blocks = [collection_index] * 10
        self.terms = collection_index.get_term_dict()

    def build_inverted_index(self):
        """
        Build the intermediate index for each block
        """
        logging.info("Building inverted index...")
        for i, block in enumerate(self.blocks):
            block_index = BSBIndex(self.collection, self.terms, block.get_document_dict(i))
            block_index.build()
            logging.info("Built block {} index".format(i))
            self.intermediate_results.append(block_index)

    def merge(self):
        """
        Merge intermediate results to build the final BSBIndex on the whole collection
        """
        logging.info("Merging intermediate results...")
        index_results = defaultdict(list)
        for result in self.intermediate_results:
            self.documents.update(result.get_documents())

            # Merge intermediate indexes
            for k, v in result.get_index().items():
                if k in index_results.keys():
                    index_results[k] += v
                else:
                    index_results[k] = v

        # Group by doc_id for each term_id
        for term_id, posting_list in index_results.items():
            parsed = groupby(sorted(posting_list, key=get_key), key=get_key)
            for doc_id, occ in parsed:
                if term_id in self.index.keys():
                    self.index[term_id].append((doc_id, sum([oc[1] for oc in occ])))
                else:
                    self.index[term_id] = [(doc_id, sum([oc[1] for oc in occ]))]

    def get_index(self):
        return self.index

    def write(self, title, json_obj):
        with open(index_path + "/" + title + "_" + self.collection + ".json", "w") as f:
            json.dump(json_obj, f)
            f.close()

    def load(self):
        with open(index_path + "/index_" + self.collection + ".json") as f:
            print(json.load(f))
            f.close()


if __name__ == "__main__":
    index = BSBI('CACM')
    # index = BSBI('CS276')  # takes at least 5 minutes to run for the 2 first folders, 7 minutes for 3 first folders
    index.build()
