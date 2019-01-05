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

    def search(self):
        results = self.evaluate()
        self.display_results(results)

    def find_in_index(self, term: str):
        """search term in the index and return the doc ids"""
        term_id = str(self.terms[term])
        return self.index[term_id]

    def all_docs_ids(self):
        return list(self.documents.keys())

    def evaluate(self):
        """returns all docIds corresponding to the search"""
        if type(self.request.first) == BooleanRequest:
            first_doc_id = self.request.first.evaluate()
        elif type(self.request.first) == str:
            first_doc_id = self.find_in_index(self.request.first)
        else:
            raise NonValidRequestException(self.request)

        if self.request.second:
            if type(self.request.second) == BooleanRequest:
                second_doc_id = self.request.second.evaluate()
            elif type(self.request.second) == str:
                second_doc_id = self.find_in_index(self.request.second)
            else:
                raise NonValidRequestException(self.request)

        if self.request.operation == Operation.NOT:
            results = [doc_id for doc_id in self.all_docs_ids() if doc_id not in first_doc_id]
            return results
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
            print(doc_id)
            print(self.documents[doc_id])
            print()


if __name__ == "__main__":
    # request_and = BooleanRequest(Operation.AND, "semiconductor", "hardware")
    request_not = BooleanRequest(Operation.NOT, "semiconductor")
    # request_not_and = BooleanRequest(Operation.NOT, request_and)
    model = BooleanEvaluation(request_not, "CACM")
    model.search()
