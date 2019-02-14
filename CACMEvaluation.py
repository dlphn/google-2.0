from BSBIndex import BSBIndex
from CACMIndex import CACMIndex
import config
import numpy as np

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


# Performance

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
    results, total = model.search(NormalizedTfIdfWeighting(), "jaccard", rank=10)
    end = time.time()
    return end - start


# Pertinence : precision, rappel, F mesure, E mesure, R mesure, Mean average precision

def calculate_measures(weighting=NaturalWeighting()):
    expected, actual = test_CACM_against_qrels(weighting)
    plot_recall_precision(expected, actual, weighting)
    calculate_r_measure(expected, actual)


def test_CACM_against_qrels(weighting):
    """

    :param weighting:
    :return: expected : the expected results for all 64 queries
            actual : the actual results given by the chosen weighting
    """

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
    for request_id, request in requests.items():
        model = VectorialEvaluation(request, "CACM")
        results = model.search(weighting)
        actual[int(request_id)] = results[0]

    return expected, actual


def plot_recall_precision(expected, actual, weighting):
    '''Plots the precision, e-measure and f-mesure relative to the recall. It is averaged over all test queries.
    Also calculates the mean average precision
    '''

    print("Plotting recall-precision curve...")
    x = [0.1*n for n in range(11)]  # recall
    y = [0.0 for _ in range(11)]  # precision
    e = [0.0 for _ in range(11)]  # e-measure
    f = [0.0 for _ in range(11)]  # f-measure
    avg_precision = [] # average precision

    for request_id in expected.keys():
        rappel, precision = calculate_recall_precision(expected[request_id], actual[request_id])
        avg_precision.append(np.average(precision))
        for j in range(11):  # approximate the precision for the given recall to get curve interpolation
            rj = x[j]
            for i,r in enumerate(rappel):
                if r > rj:
                    y[j] += max(precision[i:])
                    break
    for j in range(11):
        y[j] = y[j]/64

    # calculate e and f measure
    for j in range(11):
        e[j] += e_measure(x[j], y[j])
        f[j] += 1 - e[j]

    plt.plot(x, y, marker="x", label='precision')
    plt.plot(x, e, marker='x', label="e-measure")
    plt.plot(x, f, marker='x', label="f-measure")
    plt.axis('equal')
    plt.xlabel('Recall')
    plt.legend()
    plt.title("Recall-precision curve for the {}".format(type(weighting).__name__))
    plt.show()
    print("Recall-precision curve plotted")
    print("The Mean Average Precision is {}".format(np.nanmean(avg_precision)))


def calculate_recall_precision(expected, actual):
    recall = []
    precision = []
    relevant_results = []
    for rank in range(len(actual)):
        if actual[rank] in expected:
            relevant_results.append(actual[rank])
            recall.append(len(relevant_results)/len(expected))
            precision.append(len(relevant_results)/(rank+1))
    return recall, precision


def calculate_r_measure(expected, actual):
    for request_id in expected.keys():
        r_prec = r_precision(expected[request_id], actual[request_id])
        print("For the request {0} the r-precision is {1}.". format(request_id, r_prec))


def r_precision(expected, actual):
    r_prec = 0
    for rank in range(len(expected)):
        if len(actual) > rank and actual[rank] in expected:
            r_prec += 1
    return r_prec/len(expected)


def e_measure(rappel, precision):
    if rappel > 0:
        beta = float(precision)/float(rappel)
        e = 1 - (((beta * beta + 1) * rappel * precision) / (beta * beta * precision + rappel))
        return e
    else:
        return 1


if __name__ == "__main__":
    # Performance calculation
    print("The index is created in {}".format(index_creation_time()))
    print("The index has a size {}".format(get_file_size("index_CACM.json")))
    print("A boolean request gives a response in {}s".format(get_boolean_response_time()))
    print("A vectorial request gives a response in {}s".format(get_vectorial_response_time()))

    # Pertinence calculation
    # Here you can change the weighting and use NaturalWeighting or NormalizedTfIdfWeighting
    calculate_measures(NaturalWeighting())