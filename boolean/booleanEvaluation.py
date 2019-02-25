from boolean.booleanRequest import *
from evaluation import *


class BooleanEvaluation(Evaluation):

    def search(self):
        results = self.evaluate(self.request)
        return results

    def find_in_index(self, term: str):
        """search term in the index and return the doc ids"""
        if term not in self.terms:
            return []
        else:
            term_id = self.terms[term]
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
            elif first[p1] < second[p2]:
                p1 += 1
            else:
                p2 += 1
        return answer


if __name__ == "__main__":
    # request_and = BooleanRequest(Operation.AND, "arithmetic", "hardware")  # 1258, 1409, 2175, 3131
    # model = BooleanEvaluation(request_and, "CACM")
    request_and = BooleanRequest(Operation.AND, "1", "00")
    model = BooleanEvaluation(request_and, "CS276")
    res = model.search()
    model.display_results(res, len(res))
