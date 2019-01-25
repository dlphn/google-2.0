from config import *
from abc import ABC, abstractmethod

import json


def _decode(o):
    if isinstance(o, str):
        try:
            return int(o)
        except ValueError:
            return o
    elif isinstance(o, dict):
        return {_decode(k): v for k, v in o.items()}
    elif isinstance(o, list):
        return [_decode(v) for v in o]
    else:
        return o


class Evaluation(ABC):

    def __init__(self, request, collection):
        self.request = request
        self.collection = collection
        self.documents = self.load("documents")
        self.terms = self.load("terms")
        self.index = self.load("index")

    def load(self, file):
        with open(index_path + "/" + file + "_" + self.collection + ".json") as f:
            if file == "terms":
                text = json.load(f)
            else:
                text = json.load(f, object_hook=_decode)
            f.close()
            return text

    @abstractmethod
    def search(self):
        pass

    def display_results(self, doc_ids, total_results):
        if total_results is None:
            total_results = len(doc_ids)
        for doc_id in doc_ids:
            print(doc_id)
            print(self.documents[doc_id])
            print()
        print(str(len(doc_ids)) + " result(s) displayed")
        print("There are {} result(s) corresponding to the request.".format(total_results))
