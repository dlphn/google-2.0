from vectorial.weighting import *
import math


class TfIdfWeighting(Weighting):

    def nd(self, documents, vocab, index, terms):  # none
        return {document_id: 1 for document_id in documents.keys()}

    def pdf(self, df, nb_docs):  # idf
        return math.log10(nb_docs/df)

    def ptf(self, tf):  # logarithm
        if tf > 0:
            return 1 + math.log10(tf)
        else:
            return 0
