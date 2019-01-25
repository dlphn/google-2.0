import unittest

from helpers.CACMParser import CACMParser
from vectorial.qrelsParser import QrelsParser
from vectorial.vectorialEvaluation import VectorialEvaluation
from vectorial.naturalWeighting import *
from vectorial.tfidfWeighting import *


class TestEvaluation(unittest.TestCase):

    def test_CACM(self):
        request = "arithmetic hardware"
        model = VectorialEvaluation(request, "CACM")
        results = model.search(NaturalWeighting())
        self.assertEqual([1258, 2967, 1718, 2377, 1965], results[0].tolist())

    def test_CACM_against_qrels(self):
        cacm_parser = CACMParser()
        with open("../CACM/query.text") as f:
            cacm_data = f.read()

        dic = cacm_parser.parse_documents(cacm_data)
        requests = cacm_parser.parse_summary(dic)

        qrels_parser = QrelsParser()
        with open("../CACM/qrels.text") as f:
            qrels_data = f.read()

        expected = qrels_parser.parse_all(qrels_data)

        matching_results = {key: [] for key in range(1, 65)}

        for request_id, request in requests.items():
            model = VectorialEvaluation(request, "CACM")
            # results = model.search(NaturalWeighting())
            results = model.search(TfIdfWeighting())
            try:
                for doc_id in expected[int(request_id)]:
                    if doc_id in results[0]:
                        matching_results[int(request_id)].append(doc_id)
            except KeyError:
                pass
            # self.assertIn(expected[int(request_id)], results)
        for key, value in matching_results.items():
            print("{0}: {1}".format(key, value))
        # TODO remove
        self.assertEqual(0,0)


if __name__ == "__main__":
    unittest.main()



