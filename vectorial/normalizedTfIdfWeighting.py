from vectorial.weighting import *
import math
from vectorial.functions import *


class NormalizedTfIdfWeighting(Weighting):

    def nd(self, documents, vocab, index, terms):
        nb_docs = len(documents)
        n_d = [0] * (len(documents) + 1)
        for document_id in documents.keys():
            weight_sum = 0
            for term in vocab:
                try:
                    term_id = terms[term]  # term_id might not exist in index
                    tf_d = term_frequency_in_index(term_id, document_id, index)  # term frequency in document
                    ptf_d = self.ptf(tf_d)  # ponderation
                    df = document_frequency(term_id, index)
                    pdf = self.pdf(df, nb_docs)  # ponderation
                    w_t_d = ptf_d * pdf  # tf*idf
                    weight_sum += w_t_d
                except KeyError:
                    pass
            if weight_sum > 0:
                n_d[document_id] = 1/math.sqrt(weight_sum)
            else:
                n_d[document_id] = 1
        return n_d

    def pdf(self, df, nb_docs):  # idf
        return math.log10(nb_docs/df)

    def ptf(self, tf):  # logarithm
        if tf > 0:
            return 1 + math.log10(tf)
        else:
            return 0
