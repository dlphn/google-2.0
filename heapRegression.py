import numpy as np


class HeapRegression:
    """
    Calculate the variables of Heap law using linear regression
    """

    def __init__(self, nb_tokens, nb_vocab):
        """
        Initialize the variables used for regression

        :param nb_tokens: array of number of tokens from variable text lengths
        :param nb_vocab: array of number of vocabulary from variable text lengths
        """
        self.nb_tokens = nb_tokens
        self.nb_vocab = nb_vocab
        self.b = 0
        self.k = 0

    def calculate_regression(self):
        """
        Calculate (b,k) from Heap law: nb_vocab = k * nb_tokens ^ b
        """
        regression = np.polyfit(np.log10(self.nb_tokens), np.log10(self.nb_vocab), deg=1)
        self.b = regression[0]
        self.k = 10 ** regression[1]
        return self.b, self.k

    def calculate_vocab(self, size):
        return self.k * (size ** self.b)


if __name__ == "__main__":
    # CACM parameters, result from CACMIndex.py
    CACM_tokens = np.array([188887, 85151])
    CACM_vocab = np.array([9238, 6334])

    # CS276 parameters, result from CS276Index.py
    CS276_tokens = np.array([25527977,  12796571])
    CS276_vocab = np.array([284418, 140665])

    # Change here which collection you want to use
    heap = HeapRegression(CACM_tokens, CACM_vocab)
    # heap = HeapRegression(CS276_tokens, CS276_vocab)

    parameters = heap.calculate_regression()

    print("The Heap law parameters are:")
    print("(b, k) = {}".format(parameters))

    print("For 1 million tokens there would be (by Heap law) {} vocabulary"
          .format(heap.calculate_vocab(1000000)))


