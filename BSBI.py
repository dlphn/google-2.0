import logging
import json

from CACMIndex import CACMIndex
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

    def segment(self):
        """
        Segment collection in blocks
        """
        if self.collection == 'CACM':
            self.blocks.append(CACMIndex())

    def build_inverted_index(self):
        """
        Build the intermediate index for each block
        """
        for block in self.blocks:
            block.build()
            block_index = BSBIndex(self.collection, block.get_term_dict(), block.get_document_dict())
            block_index.build()
            self.intermediate_results.append(block_index)

    def merge(self):
        """
        Merge intermediate results to build the final BSBIndex on the whole collection
        """
        print(self.intermediate_results[0].get_index())
        # Merge everything...
        self.index = self.intermediate_results[0].get_index()
        self.terms = self.intermediate_results[0].get_terms()
        self.documents = self.intermediate_results[0].get_documents()

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
    index.build()
    print(index.get_index())
