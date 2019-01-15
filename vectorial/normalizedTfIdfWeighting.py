from vectorial.weighting import *
import math


class NormalizedTfIdfWeighting(Weighting):

    def nd(self, vocab):  # cosine
        return 1  # 1/sum(w_i_d) for i in vocab

    def pdf(self, df, N):  # idf
        return math.log10(N/df)

    def ptf(self, tf):  # logarithm
        if tf > 0:
            return 1 + math.log10(tf)
        else:
            return 0
