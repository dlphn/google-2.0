import math


class SimilarityMeasure:

    def __init__(self, measure='cosine'):
        self.measure = measure

    def compute(self, sim, n_d, n_q):
        if self.measure == 'jaccard':
            return self.jaccard(sim, n_d, n_q)
        elif self.measure == 'dice':
            return self.dice(sim, n_d, n_q)
        else:
            return self.cosine(sim, n_d, n_q)

    @staticmethod
    def cosine(sim, n_d, n_q):
        return sim / (math.sqrt(n_d) * math.sqrt(n_q))

    @staticmethod
    def jaccard(sim, n_d, n_q):
        return sim / (n_d + n_q - sim)

    @staticmethod
    def dice(sim, n_d, n_q):
        return 2 * sim / (n_d + n_q)
