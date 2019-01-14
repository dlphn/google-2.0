from abc import ABC, abstractmethod


class Weighting(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def nd(self, vocab):
        pass

    @abstractmethod
    def pdf(self, df, N):
        pass

    @abstractmethod
    def ptf(self, tf):
        pass
