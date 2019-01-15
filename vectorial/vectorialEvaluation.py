from evaluation import *
from helpers.textProcessing import *
import math
import collections
import numpy
from vectorial.naturalWeighting import *


class VectorialEvaluation(Evaluation):

    def search(self, weighting=NaturalWeighting()):
        # request has to be preprocessed to get vocab and frequency
        processor = TextProcessor(self.collection)
        result = processor.process(self.request)
        request_vocab = list(result[1])
        request_vocab_full = result[3]
        documents, similarity = self.calculate_similarity(request_vocab, request_vocab_full, weighting)
        print(documents[:5], similarity[:5])

    def calculate_similarity(self, request_vocab, request_vocab_full, weighting):
        n_q = 0
        nb_docs = len(self.documents)
        sim = [0] * nb_docs
        n_d = weighting.nd(self.documents, request_vocab)  # ponderation => entire index vocab ?
        counter = collections.Counter(request_vocab_full)
        for i in range(len(request_vocab)):
            term_id = str(self.terms[request_vocab[i]])
            tf_q = counter[request_vocab[i]]  # term frequency in request a modifier
            ptf_q = weighting.ptf(tf_q)  # ponderation
            df = len(self.index[term_id])
            pdf = weighting.pdf(df, nb_docs)  # ponderation
            w_t_q = ptf_q * pdf
            n_q += w_t_q * w_t_q
            L = self.index[term_id]
            for doc in L:
                doc_id = int(doc[0])
                tf_d = doc[1]  # term frequency in document
                ptf_d = weighting.ptf(tf_d)  # ponderation
                w_t_d = n_d[doc_id] * ptf_d * pdf
                sim[doc_id] += w_t_q * w_t_d

        for j in range(nb_docs):
            if sim[j] != 0:
                sim[j] = (sim[j] / (math.sqrt(n_d[j]) * math.sqrt(n_q)))

        sorted_docs = numpy.argsort(sim)[::-1]
        sim.sort(reverse=True)
        return sorted_docs, sim


if __name__ == "__main__":
    request = "arithmetic hardware"
    model = VectorialEvaluation(request, "CACM")
    model.search(NaturalWeighting())
