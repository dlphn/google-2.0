import numpy as np

class HeapRegression:
    '''Calculate the variables of Heap law using linear regression
    '''

    def __init__(self, tokens, voca):
        '''Initialize the variables used for the regression

        :param tokens: array of number of tokens from variable text lengths
        :param voca: array of number of vocabulary grom variable text lengths
        '''
        self.tokens = tokens
        self.voca = voca

    def calculate_regression(self):
        '''Calculate (b,k) from Heap law: nb_voca = k * nb_token ^ b
        '''
        regression = np.polyfit(np.log10(self.tokens), np.log10(self.voca), deg=1)
        b = regression[0]
        k = 10 ** regression[1]
        return (b,k)

    def calculate_voca(self, T, param):
        b = param[0]
        k = param[1]
        return k * (T ** b)


if __name__ == "__main__":
    # CACM parameters, result from CACMIndex.py
    CACM_tokens = np.array([188887, 85151])
    CACM_voca = np.array([9238, 6334])

    # CS276 parameters, resul from CS276Index.py
    CS276_tokens = np.array([25527977,  12796571])
    CS276_voca = np.array([17062207, 8417188])

    # CS276 parameters

    heap = HeapRegression(CACM_tokens, CACM_voca)
    # heap = HeapRegression(CS276_tokens, CS276_voca)

    parameters = heap.calculate_regression()

    print("(b, k) = {}".format(parameters))

    print("For 1 million tokens there would be (by Heap law) {} vocalubary"
          .format(heap.calculate_voca(1000000, parameters)))


