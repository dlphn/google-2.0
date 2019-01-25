import collections


def term_frequency(term, vocab_full):
    """
    Occurrences of terms in the full vocabulary
    """
    occurrences = collections.Counter(vocab_full)  # get occurrences of each term
    return occurrences[term]


def document_frequency(term_id, index):
    """
    Number of documents in which the term appears
    """
    posting_list = index[term_id]
    return len(posting_list)
