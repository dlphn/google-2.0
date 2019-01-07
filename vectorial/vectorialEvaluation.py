from evaluation import *
import math

class VectorialEvaluation(Evaluation):

    def evaluate(self, request):
        #request has to be preprocessed to get vocab and frequency
        pass

    def calculate_similarity(self, request_vocab):
        n_q = 0
        N = len(self.documents)
        sim = [0]*N
        n_d = [0] * N # a modifier
        for i in range(len(request_vocab)):
            tf_q = 0
            ptf_q = tf_q / len(request_vocab)
            term_id = self.terms[request_vocab[i]]
            df = len(self.index[term_id])
            pdf = float(df) / N
            w_t_q = ptf_q * pdf
            n_q += w_t_q * w_t_q
            L = self.index[term_id]
            for doc in L:
                tf_d = 0
                ptf_d = 0 # need document vocab
                w_t_d = n_d[j] * ptf_d * pdf
                sim[j] += w_t_d * w_t_d

        for j in range(N):
            if sim[j] != 0:
                sim[j] = sim[j] / (math.sqrt(n_d[j]) * math.sqrt(n_q))


