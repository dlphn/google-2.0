from vectorial.weighting import *


class NaturalWeighting(Weighting):

    def nd(self, vocab):
        return 1

    def pdf(self, df, N):
        return 1

    def ptf(self, tf):
        return tf
