from config import *

import json


class Evaluation:

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
