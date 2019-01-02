import numpy as np


class HeapRegression:
    """Calculate the variables of Heap law using linear regression
    """

    def __init__(self, tokens, vocab):
        """Initialize the variables used for the regression

        :param tokens: array of number of tokens from variable text lengths
        :param vocab: array of number of vocabulary from variable text lengths
        """
        self.tokens = tokens
        self.vocab = vocab

    def calculate_regression(self):
        """Calculate (b,k) from Heap law: nb_vocab = k * nb_token ^ b
        """
        regression = np.polyfit(np.log10(self.tokens), np.log10(self.vocab), deg=1)
        b = regression[0]
        k = 10 ** regression[1]
        return b, k

    def calculate_vocab(self, T, param):
        b = param[0]
        k = param[1]
        return k * (T ** b)


if __name__ == "__main__":
    # CACM parameters, result from CACMIndex.py
    CACM_tokens = np.array([188887, 85151])
    CACM_vocab = np.array([9238, 6334])

    # CS276 parameters, result from CS276Index.py
    CS276_tokens = np.array([25527977,  12796571])
    CS276_vocab = np.array([17062207, 8417188])

    # CS276 parameters

    heap = HeapRegression(CACM_tokens, CACM_vocab)
    # heap = HeapRegression(CS276_tokens, CS276_vocab)

    parameters = heap.calculate_regression()

    print("(b, k) = {}".format(parameters))

    print("For 1 million tokens there would be (by Heap law) {} vocabulary"
          .format(heap.calculate_vocab(1000000, parameters)))


