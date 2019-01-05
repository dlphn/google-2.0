from boolean.booleanRequest import *
from config import *

import json


class BooleanEvaluation:
    def __init__(self, request, collection):
        self.request = request
        self.collection = collection
        self.index = self.load("index")
        self.documents = self.load("documents")
        self.terms = self.load("terms")

    def load(self, file):
        with open(index_path + "/" + file + "_" + self.collection + ".json") as f:
            return json.load(f)
            f.close()

    def find_in_index(self, term: str):
        """search term in the index and return the doc ids"""
        term_id = self.terms[term]  # str ?
        return self.index[term_id]

    def all_docs_ids(self):
        return

    def evaluate(self):
        """returns all docIds corresponding to the search"""
        if self.request.first.type == BooleanRequest:
            first_doc_id = self.request.first.evaluate_cacm()
        elif self.request.first.type == str:
            first_doc_id = self.find_in_index(self.request.first)
        else:
            raise NonValidRequestException(self.request)

        if self.request.second.type == BooleanRequest:
            second_doc_id = self.request.second.evaluate_cacm()
        elif self.request.first.type == str:
            second_doc_id = self.find_in_index(self.request.second)
        else:
            raise NonValidRequestException(self.request)

        if self.request.operation == Operation.NOT:
            return self.all_docs_ids().remove(first_doc_id)
        elif self.request.operation == Operation.AND:  # à modifier
            result = []
            for doc in first_doc_id:
                if doc in second_doc_id:
                    result.append(doc)
            return result
        elif self.request.operation == Operation.OR:
            return first_doc_id.append(second_doc_id)
        else:
            raise NonValidRequestException(self.request)

    def display_results(self, doc_ids):
        for doc_id in doc_ids:
            print(self.documents[doc_id])
