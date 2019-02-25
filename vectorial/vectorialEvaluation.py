import logging
from evaluation import *
from helpers.textProcessing import *
from vectorial.naturalWeighting import *
from vectorial.tfidfWeighting import *
from vectorial.normalizedTfIdfWeighting import *
from vectorial.similarityMeasure import *
from vectorial.functions import *

logging.basicConfig(format='%(asctime)s - %(levelname)s : %(message)s', level=logging.INFO)


class VectorialEvaluation(Evaluation):

    def search(self, weighting=NaturalWeighting(), measure='cosine', rank=-1):
        '''Returns 10 first results of the search'''
        # request has to be preprocessed to get vocab and frequency
        processor = TextProcessor(self.collection)
        result = processor.process(self.request)
        request_vocab = list(result[1])
        request_vocab_full = result[3]
        documents, similarity = self.calculate_similarity(request_vocab, request_vocab_full, weighting, measure)
        # print(documents[:5], similarity[:5])
        # self.display_results(documents[:5])
        pertinent_doc = [documents[i] for i in range(len(documents)) if similarity[i] > 0]
        total_nb = len(pertinent_doc)  # nb of documents of similarity > 0
        if rank >= 0:
            return documents[:rank], total_nb
        else:
            return pertinent_doc, total_nb

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
        sim = {document_id: 0 for document_id in self.documents.keys()}
        n_d = weighting.nd(self.documents, request_vocab, self.index, self.terms)

        for request_term in request_vocab:
            try:
                term_id = self.terms[request_term]

                tf_q = term_frequency(request_term, request_vocab_full)  # term frequency in request
                ptf_q = weighting.ptf(tf_q)

                df = document_frequency(term_id, self.index)
                pdf = weighting.pdf(df, nb_docs)

                w_t_q = ptf_q * pdf  # tf*idf
                n_q += w_t_q * w_t_q

                posting_list = self.index[term_id]
                for doc in posting_list:
                    doc_id = doc[0]
                    tf_d = doc[1]  # term frequency in document
                    ptf_d = weighting.ptf(tf_d)
                    w_t_d = n_d[doc_id] * ptf_d * pdf
                    sim[doc_id] += w_t_q * w_t_d

            except KeyError:
                print("key error")
                pass

        for j in self.documents.keys():
            # compute similarity between request vector and documents vectors
            if sim[j] != 0:
                measure = SimilarityMeasure(measure)
                sim[j] = measure.compute(sim[j], n_d[j], n_q)

        sorted_docs = []
        sorted_sim = []
        # sort documents by similarity (greatest to lowest)
        for doc_id, similarity in sorted(sim.items(), key=lambda x: x[1], reverse=True):
            sorted_docs.append(doc_id)
            sorted_sim.append(similarity)
        return sorted_docs, sorted_sim


if __name__ == "__main__":
    logging.info("Start search...")
    cs276_request = "data processing high res calibration"
    cacm_request = "arithmetic hardware"
    model = VectorialEvaluation(cs276_request, "CS276")
    # model = VectorialEvaluation(cacm_request, "CACM")
    # results, total = model.search(NaturalWeighting())
    # results, total = model.search(TfIdfWeighting())
    results, total = model.search(NormalizedTfIdfWeighting(), "jaccard")
    print(results)
    model.display_results(results, total)
    logging.info("Results retrieved.")
