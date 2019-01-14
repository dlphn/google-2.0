from evaluation import *
from helpers.textProcessing import *
import math
import collections
import numpy


class VectorialEvaluation(Evaluation):

    def search(self):
        # request has to be preprocessed to get vocab and frequency
        processor = TextProcessor(self.collection)
        result = processor.process(self.request)
        request_vocab = list(result[1])
        request_vocab_full = result[3]
        documents, similarity = self.calculate_similarity(request_vocab, request_vocab_full)
        print(documents[:5], similarity[:5])

    def calculate_similarity(self, request_vocab, request_vocab_full):
        n_q = 1
        N = len(self.documents)
        sim = [0] * N
        n_d = [1] * N  # a modifier
        counter = collections.Counter(request_vocab_full)
        for i in range(len(request_vocab)):
            term_id = str(self.terms[request_vocab[i]])
            tf_q = counter[request_vocab[i]]  # term frequency in request a modifier
            ptf_q = tf_q  # a modifier
            df = len(self.index[term_id])
            pdf = 1  # a modifier
            w_t_q = ptf_q * pdf
            n_q += w_t_q * w_t_q
            L = self.index[term_id]
            for doc in L:
                tf_d = doc[1]  # term frequency in document
                ptf_d = tf_d  # need document vocab
                w_t_d = n_d[int(doc[0])] * ptf_d * pdf
                sim[int(doc[0])] += w_t_q * w_t_d

        for j in range(N):
            if sim[j] != 0:
                sim[j] = (sim[j] / (math.sqrt(n_d[j]) * math.sqrt(n_q)))

        sorted_docs = numpy.argsort(sim)[::-1]
        sim.sort(reverse=True)
        return sorted_docs, sim


if __name__ == "__main__":
    request = "arithmetic hardware"
    model = VectorialEvaluation(request, "CACM")
    model.search()
