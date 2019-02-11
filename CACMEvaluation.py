from BSBIndex import BSBIndex
from CACMIndex import CACMIndex
import config

import time
import os
from hurry.filesize import size
import matplotlib.pyplot as plt

from boolean.booleanEvaluation import BooleanEvaluation
from boolean.booleanRequest import *
from helpers.CACMParser import CACMParser
from vectorial.qrelsParser import QrelsParser
from vectorial.vectorialEvaluation import VectorialEvaluation, NormalizedTfIdfWeighting, TfIdfWeighting, \
    NaturalWeighting


# Performance : temps de calcul indexation, temps de réponse requete, espace disque index


def index_creation_time():
    start = time.time()
    cacm = CACMIndex()
    cacm.build()
    index = BSBIndex('CACM', cacm.get_term_dict(), cacm.get_document_dict())
    index.build()
    end = time.time()

    return end-start


def get_file_size(filename):
    return size(os.path.getsize(config.index_path + "/" + filename))


def get_boolean_response_time():
    request_and = BooleanRequest(Operation.AND, "arithmetic", "hardware")  # 1258, 1409, 2175, 3131
    model = BooleanEvaluation(request_and, "CACM")
    start = time.time()
    res = model.search()
    end = time.time()
    return end - start


def get_vectorial_response_time():
    request = "arithmetic hardware"
    model = VectorialEvaluation(request, "CACM")
    start = time.time()
    results, total = model.search(NormalizedTfIdfWeighting(), "jaccard")
    end = time.time()
    return end - start


# print("The index is created in {}".format(index_creation_time()))
# print("The index has a size {}".format(get_file_size("index_CACM.json")))
# print("A boolean request gives a response in {}s".format(get_boolean_response_time()))
# print("A vectorial request gives a response in {}s".format(get_vectorial_response_time()))


# Pertinence : precision, rappel, F mesure, E mesure, R mesure, Mean average precision

def test_CACM_against_qrels():
    cacm_parser = CACMParser()
    with open("./CACM/query.text") as f:
        cacm_data = f.read()

    dic = cacm_parser.parse_documents(cacm_data)
    requests = cacm_parser.parse_summary(dic)

    qrels_parser = QrelsParser()
    with open("./CACM/qrels.text") as f:
        qrels_data = f.read()

    expected = qrels_parser.parse_all(qrels_data)
    actual = {key: [] for key in range(1, 65)}

    matching_results = {key: [] for key in range(1, 65)}

    for request_id, request in requests.items():
        model = VectorialEvaluation(request, "CACM")
        # results = model.search(NaturalWeighting())
        results = model.search_all(TfIdfWeighting())
        actual[int(request_id)] = results[0]
        try:
            for doc_id in expected[int(request_id)]:
                if doc_id in results[0]:
                    matching_results[int(request_id)].append(doc_id)
        except KeyError:
            pass
        # self.assertIn(expected[int(request_id)], results)
    for key, value in matching_results.items():
        print("{0}: {1}".format(key, value))
        print("actual: {}".format(actual[key]))
    return expected, actual, matching_results


def courbe_rappel_precision():
    expected, actual, matching_results = test_CACM_against_qrels()
    x = [0.1*n for n in range(10)]
    y = [0.0 for _ in range(10)]
    for request_id in expected.keys():
        rappel, precision = courbe(expected[request_id], actual[request_id])
        for j in range(10):
            rj = x[j]
            for i,r in enumerate(rappel):
                if r > rj:
                    y[j] += max(precision[i:])
                    break
    for j in range(10):
        y[j] = y[j]/64
    plt.plot(x, y, marker="x")
    plt.axis('equal')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.show()


def courbe(expected, actual):
    r = []
    p = []
    relevant_results = []
    for rank in range(len(actual)):
        if actual[rank] in expected:
            relevant_results.append(actual[rank])
            r.append(len(relevant_results)/len(expected))
            p.append(len(relevant_results)/(rank+1))
    return r, p


courbe_rappel_precision()