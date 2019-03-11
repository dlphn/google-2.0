import unittest

from helpers.CACMParser import CACMParser
from vectorial.qrelsParser import QrelsParser
from vectorial.vectorialEvaluation import VectorialEvaluation
from vectorial.naturalWeighting import *
from vectorial.normalizedTfIdfWeighting import *


class TestEvaluation(unittest.TestCase):

    def test_CACM(self):
        request = "arithmetic hardware"
        model = VectorialEvaluation(request, "CACM")
        results, total = model.search(NaturalWeighting(), rank=5)
        self.assertEqual([1258, 1718, 2967, 1409, 1965], results)

    def test_CS276(self):
        request = "data processing high res calibration"
        model = VectorialEvaluation(request, "CS276")
        results, total = model.search(NormalizedTfIdfWeighting(), "jaccard", rank=5)
        self.assertEqual(['2-4486', '5-8718', '5-8719', '2-3500', '7-6004'], results)


if __name__ == "__main__":
    unittest.main()



