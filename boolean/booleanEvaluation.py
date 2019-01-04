from boolean.booleanRequest import *


class BooleanEvaluation:
    def __init__(self, request, index):
        self.request = request
        self.index = index

    def find_in_index(self, term: str):
        '''search term in the index and returns the doc ids'''
        return

    def all_docs_ids(self):
        return

    def evaluate(self):
        '''returns all docIds correspondinf to the search'''
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
        elif self.request.operation == Operation.AND:
            result = []
            for doc in first_doc_id:
                if doc in second_doc_id:
                    result.append(doc)
            return result
        elif self.request.operation == Operation.OR:
            return first_doc_id.append(second_doc_id)
        else:
            raise NonValidRequestException(self.request)
