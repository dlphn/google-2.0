from vectorial.weighting import *
import math


class TfIdfWeighting(Weighting):

    def nd(self, documents, vocab):  # none
        return [1] * len(documents)

    def pdf(self, df, nb_docs):  # idf
        return math.log10(nb_docs/df)

    def ptf(self, tf):  # logarithm
        if tf > 0:
            return 1 + math.log10(tf)
        else:
            return 0
