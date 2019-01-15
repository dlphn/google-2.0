from vectorial.weighting import *
import math


class TfIdfWeighting(Weighting):

    def nd(self, vocab):  # none
        return 1

    def pdf(self, df, N):  # idf
        return math.log10(N/df)

    def ptf(self, tf):  # logarithm
        if tf > 0:
            return 1 + math.log10(tf)
        else:
            return 0
