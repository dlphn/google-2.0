import unittest

from helpers.CACMParser import CACMParser
from vectorial.vectorialEvaluation import VectorialEvaluation
from vectorial.naturalWeighting import *
from vectorial.tfidfWeighting import *


class TestEvaluation(unittest.TestCase):

    def test_simple_CACM_vectorial(self):
        request = "arithmetic hardware"
        model = VectorialEvaluation(request, "CACM")
        results = model.search(NaturalWeighting())
        self.assertEqual(results.tolist(), [1258, 2967, 1718, 2744, 1409])

    def test_CACM_vectorial(self):
        parser = CACMParser()
        with open("../CACM/query.text") as f:
            read_data = f.read()

        dic = parser.parse_documents(read_data)
        requests = parser.parse_summary(dic)

        for request_id, request in requests.items():
            model = VectorialEvaluation(request, "CACM")
            # results = model.search(NaturalWeighting())
            results = model.search(TfIdfWeighting())
            print(request_id, results)
            self.assertEqual(0, 0)


if __name__ == "__main__":
    unittest.main()



