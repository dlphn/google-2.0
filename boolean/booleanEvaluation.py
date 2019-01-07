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
        results = self.evaluate(self.request)
        print(results)
        # self.display_results(results)

    def find_in_index(self, term: str):
        """search term in the index and return the doc ids"""
        term_id = str(self.terms[term])
        return [doc_id[0] for doc_id in self.index[term_id]]

    def all_docs_ids(self):
        return list(self.documents.keys())

    def evaluate(self, request):
        """returns all docIds corresponding to the search"""
        first_doc_id, second_doc_id = [], []

        if type(request.first) == BooleanRequest:
            first_doc_id = self.evaluate(request.first)
        elif type(request.first) == str:
            first_doc_id = self.find_in_index(request.first)
        else:
            raise NonValidRequestException(request)

        if request.second:
            if type(request.second) == BooleanRequest:
                second_doc_id = self.evaluate(request.second)
            elif type(request.second) == str:
                second_doc_id = self.find_in_index(request.second)
            else:
                raise NonValidRequestException(request)

        if request.operation == Operation.NOT:
            results = [doc_id for doc_id in self.all_docs_ids() if doc_id not in first_doc_id]
            return results
        elif request.operation == Operation.AND:
            return self.intersect(first_doc_id, second_doc_id)
        elif request.operation == Operation.OR:
            return first_doc_id + second_doc_id
        else:
            raise NonValidRequestException(request)

    @staticmethod
    def intersect(first, second):
        answer = []
        p1, p2 = 0, 0
        while p1 < len(first) and p2 < len(second):
            if first[p1] == second[p2]:
                answer.append(first[p1])
                p1 += 1
                p2 += 1
            elif int(first[p1]) < int(second[p2]):
                p1 += 1
            else:
                p2 += 1
        return answer

    def display_results(self, doc_ids):
        for doc_id in doc_ids:
            print(doc_id)
            print(self.documents[doc_id])
            print()
        print(str(len(doc_ids)) + " result(s) retrieved")


if __name__ == "__main__":
    request_and = BooleanRequest(Operation.AND, "arithmetic", "hardware")  # 1258, 1409, 2175, 3131
    request_not = BooleanRequest(Operation.NOT, BooleanRequest(Operation.NOT, "semiconductor"))  # 2516
    request_or = BooleanRequest(Operation.OR, "arithmetic", "hardware")
    request_not_and = BooleanRequest(Operation.NOT, request_and)  # all but 1258, 1409, 2175, 3131
    model = BooleanEvaluation(request_not, "CACM")
    model.search()
