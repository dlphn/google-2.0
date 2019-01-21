from vectorial.weighting import *


class NaturalWeighting(Weighting):

    def nd(self, documents, vocab):
        return [1] * (len(documents) + 1)

    def pdf(self, df, nb_docs):
        return 1

    def ptf(self, tf):
        return tf
