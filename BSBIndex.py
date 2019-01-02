import logging
from itertools import groupby

from CACMIndex import CACMIndex
from helpers import textProcessing

logging.basicConfig(format='%(asctime)s - %(levelname)s : %(message)s', level=logging.INFO)


def get_key(item):
    return item[0]


class BSBIndex:
    """
    Build a Block Sort-based index
    """

    def __init__(self, collection, terms, documents):
        self.collection = collection
        self.terms = terms
        self.documents = documents
        self.index = {}
        self.parsed = []

    def build(self):
        self.parse_documents()
        self.invert()
        return self.index

    def parse_documents(self):
        """
        Parse each document as a tuple (term_id, doc_id)
        """
        for doc_id, doc in self.documents.items():
            processor = textProcessing.TextProcessor(self.collection)
            doc_terms = processor.process(doc)[1]  # vocabulary
            for term in doc_terms:
                term_id = self.terms[term]
                pair = (term_id, doc_id)
                self.parsed.append(pair)

    def invert(self):
        """
        Sort the tuples and group by term_id
        """
        self.parsed = groupby(sorted(self.parsed, key=get_key), key=get_key)
        for term_id, doc_id in self.parsed:
            self.index[term_id] = [doc[1] for doc in doc_id]


if __name__ == "__main__":
    CACMIndex = CACMIndex()
    CACMIndex.build()
    index = BSBIndex('CACM', CACMIndex.get_term_dict(), CACMIndex.get_document_dict())
    print(index.build())
