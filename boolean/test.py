import unittest

from boolean.booleanEvaluation import BooleanEvaluation
from boolean.booleanRequest import BooleanRequest, Operation


class BooleanTestEvaluation(unittest.TestCase):

    def test_CACM_and(self):
        request_and = BooleanRequest(Operation.AND, "arithmetic", "hardware")
        model = BooleanEvaluation(request_and, "CACM")
        self.assertEqual(['1258', '1409', '2175', '3131'], model.search())

    def test_CACM_not(self):
        request_not = BooleanRequest(Operation.NOT, BooleanRequest(Operation.NOT, "semiconductor"))
        model = BooleanEvaluation(request_not, "CACM")
        self.assertEqual(['2516'], model.search())

    def test_CACM_or(self):
        # (not ((not arithmetic) or (not hardware))) = arithmetic and hardware
        request_or = BooleanRequest(Operation.NOT, BooleanRequest(Operation.OR, BooleanRequest(Operation.NOT, "arithmetic"), BooleanRequest(Operation.NOT, "hardware")))
        model = BooleanEvaluation(request_or, "CACM")
        self.assertEqual(['1258', '1409', '2175', '3131'], model.search())


if __name__ == "__main__":
    unittest.main()
