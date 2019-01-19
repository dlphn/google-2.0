from vectorial.weighting import *
import math


class NormalizedTfIdfWeighting(Weighting):

    def nd(self, documents, vocab):  # cosine
        return 1  # 1/sum(w_i_d) for i in vocab, w_i_d = poids du terme ti de la requête dans le document d

    def pdf(self, df, nb_docs):  # idf
        return math.log10(nb_docs/df)

    def ptf(self, tf):  # logarithm
        if tf > 0:
            return 1 + math.log10(tf)
        else:
            return 0
