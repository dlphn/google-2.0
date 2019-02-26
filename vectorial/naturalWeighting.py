from vectorial.weighting import *


class NaturalWeighting(Weighting):

    def nd(self, documents, vocab, index, terms):
        return {document_id: 1 for document_id in documents.keys()}

    def pdf(self, df, nb_docs):
        return 1

    def ptf(self, tf):
        return tf
