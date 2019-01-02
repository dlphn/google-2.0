import logging
from CACMIndex import CACMIndex
from helpers import textProcessing

logging.basicConfig(format='%(asctime)s - %(levelname)s : %(message)s', level=logging.INFO)


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
        print(self.terms)
        self.parse_documents()
        print(self.parsed)

    def parse_documents(self):
        for docID, doc in self.documents.items():
            processor = textProcessing.TextProcessor(self.collection)
            processor.process(doc)
            doc_terms = processor.get_vocabulary_full()
            for term in doc_terms:
                pair = (term, docID)
                self.parsed.append(pair)


if __name__ == "__main__":
    CACMIndex = CACMIndex()
    CACMIndex.build()
    index = BSBIndex('CACM', CACMIndex.get_termID(), CACMIndex.get_documentID())
    index.build()
