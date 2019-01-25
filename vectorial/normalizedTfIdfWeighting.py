from vectorial.weighting import *
import math
from vectorial.functions import *


class NormalizedTfIdfWeighting(Weighting):

    def nd(self, documents, vocab):
        pass

    def nd_norm(self, documents, vocab, index, terms):  # cosine
        nb_docs = len(documents)
        n_d = [0] * (len(documents) + 1)
        for document_id, document in enumerate(documents):
            weight_sum = 0
            for term in vocab:
                try:
                    term_id = str(terms[term])  # term_id might not exist in index
                    tf_d = term_frequency_in_index(term, document, index)  # term frequency in document
                    print(tf_d)
                    ptf_q = self.ptf(tf_d)  # ponderation
                    df = document_frequency(term_id, index)
                    pdf = self.pdf(df, nb_docs)  # ponderation
                    w_t_d = ptf_q * pdf  # tf*idf
                    print(w_t_d)
                    weight_sum += w_t_d
                except KeyError:
                    print('error')
                    pass
            if weight_sum > 0:
                n_d[document_id] = 1/math.sqrt(weight_sum)
            else:
                n_d[document_id] = 1
        return n_d  # 1/sum(w_i_d) for i in vocab, w_i_d = poids du terme ti de la requête dans le document d

    def pdf(self, df, nb_docs):  # idf
        return math.log10(nb_docs/df)

    def ptf(self, tf):  # logarithm
        if tf > 0:
            return 1 + math.log10(tf)
        else:
            return 0
