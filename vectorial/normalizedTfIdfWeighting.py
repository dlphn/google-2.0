from vectorial.weighting import *
import math
from vectorial.functions import *


class NormalizedTfIdfWeighting(Weighting):

    def nd(self, documents, vocab, vocab_full, index):  # cosine
        nb_docs = len(documents)
        n_d = [0] * (len(documents) + 1)
        for document_id, document in enumerate(documents):
            for term in vocab:
                try:
                    term_id = str(terms[term])
                    tf_q = term_frequency(term, doc_vocab_full)  # term frequency in document
                    ptf_q = self.ptf(tf_q)  # ponderation
                    df = document_frequency(term_id, index)
                    pdf = self.pdf(df, nb_docs)  # ponderation
                    w_t_q = ptf_q * pdf  # tf*idf
                    sum += w_t_q
                except KeyError:
                    pass
            n_d[document_id] = 1/math.sqrt(sum)

        return 1  # 1/sum(w_i_d) for i in vocab, w_i_d = poids du terme ti de la requête dans le document d

    def pdf(self, df, nb_docs):  # idf
        return math.log10(nb_docs/df)

    def ptf(self, tf):  # logarithm
        if tf > 0:
            return 1 + math.log10(tf)
        else:
            return 0
