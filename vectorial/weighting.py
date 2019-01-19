from abc import ABC, abstractmethod


class Weighting(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def nd(self, documents, vocab):
        pass

    @abstractmethod
    def pdf(self, df, nb_docs):
        pass

    @abstractmethod
    def ptf(self, tf):
        pass
