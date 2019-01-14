from config import *
from abc import ABC, abstractmethod

import json


class Evaluation(ABC):

    def __init__(self, request, collection):
        self.request = request
        self.collection = collection
        self.index = self.load("index")
        self.documents = self.load("documents")
        self.terms = self.load("terms")

    def load(self, file):
        with open(index_path + "/" + file + "_" + self.collection + ".json") as f:
            text = json.load(f)
            f.close()
            return text

    def search(self):
        results = self.evaluate(self.request)
        print(results)
        # self.display_results(results)

    @abstractmethod
    def search(self):
        pass
