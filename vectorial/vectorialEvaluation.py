from evaluation import *
from helpers.textProcessing import *
import collections
import numpy
from vectorial.naturalWeighting import *
from vectorial.similarityMeasure import *


class VectorialEvaluation(Evaluation):

    def search(self, weighting=NaturalWeighting(), measure='cosine'):
        # request has to be preprocessed to get vocab and frequency
        processor = TextProcessor(self.collection)
        result = processor.process(self.request)
        request_vocab = list(result[1])
        request_vocab_full = result[3]
        documents, similarity = self.calculate_similarity(request_vocab, request_vocab_full, weighting, measure)
        # print(documents[:5], similarity[:5])
        # self.display_results(documents[:5])
        return documents[:10]

    def calculate_similarity(self, request_vocab, request_vocab_full, weighting, measure):
        """
        Build documents and request vectors and compute similarity.

        :param request_vocab: request terms
        :param request_vocab_full: request terms with duplicates
        :param weighting: natural / tf-idf / normalized tf-idf
        :param measure: cosine / Jaccard / Dice
        :return: list of documents ordered by decreasing similarity measure
        """
        n_q = 0
        nb_docs = len(self.documents)
        sim = [0] * (nb_docs + 1)
        n_d = weighting.nd(self.documents, request_vocab)  # ponderation
        counter = collections.Counter(request_vocab_full)  # get occurrences of each term
        for i in range(len(request_vocab)):
            try:
                term_id = str(self.terms[request_vocab[i]])
                tf_q = counter[request_vocab[i]]  # term frequency in request a modifier
                ptf_q = weighting.ptf(tf_q)  # ponderation
                df = len(self.index[term_id])
                pdf = weighting.pdf(df, nb_docs)  # ponderation
                w_t_q = ptf_q * pdf  # tf*idf
                n_q += w_t_q * w_t_q

                posting_list = self.index[term_id]
                for doc in posting_list:
                    doc_id = int(doc[0])
                    tf_d = doc[1]  # term frequency in document
                    ptf_d = weighting.ptf(tf_d)  # ponderation
                    w_t_d = n_d[doc_id] * ptf_d * pdf
                    sim[doc_id] += w_t_q * w_t_d
            except KeyError:
                pass

        for j in range(nb_docs):
            # compute similarity between request vector and documents vectors
            if sim[j] != 0:
                measure = SimilarityMeasure(measure)
                sim[j] = measure.compute(sim[j], n_d[j], n_q)

        sorted_docs = numpy.argsort(sim)[::-1]
        sim.sort(reverse=True)
        return sorted_docs, sim


if __name__ == "__main__":
    request = "arithmetic hardware"
    model = VectorialEvaluation(request, "CACM")
    results = model.search(NaturalWeighting())
    print(results)
    model.display_results(results)
