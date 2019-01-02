import os
import indexBuilder

from frequencyRankGraph import *



class CS276Index:

    def __init__(self):
        self.index = None

    def build(self):
        data = ""
        for file_id in range(10):
            for filename in os.listdir("pa1-data/" + str(file_id)):
                with open("pa1-data/" + str(file_id) + "/" + filename) as f:
                    read_data = f.read()
                    data = data + read_data
        self.index = indexBuilder.IndexBuilder('CS276', data)
        self.index.build()
        self.index.get_size()

    def get_tokens(self):
        print(self.index.get_tokens())

    def get_vocabulary(self):
        print(self.index.get_vocabulary())

    def get_freq(self):
        return self.index.get_freq()


if __name__ == "__main__":
    index = CS276Index()
    index.build()
    # index.get_tokens()
    # index.get_vocabulary()

    graph = FrequencyRankGraph(index.get_freq())
    graph.draw_graph()
    graph.draw_log_graph()





