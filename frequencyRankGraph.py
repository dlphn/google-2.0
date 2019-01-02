import matplotlib.pyplot as plt
import numpy as np


class FrequencyRankGraph:

    def __init__(self, freq):
        self.freq = [value for value in freq.values()]
        self.freq.sort(reverse=True)
        self.rank = [i for i in range(1, len(freq)+1)]

    def draw_graph(self):
        plt.plot(self.rank, self.freq)
        plt.xlabel("Rank")
        plt.ylabel("Frequency")
        plt.show()

    def draw_log_graph(self):
        plt.plot(np.log10(self.rank), np.log10(self.freq))
        plt.xlabel("log10(Rank)")
        plt.ylabel("log10(Frequency)")
        plt.show()
