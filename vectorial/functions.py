import collections


def term_frequency(term, vocab_full):
    """
    Occurrences of terms in the full vocabulary
    """
    occurrences = collections.Counter(vocab_full)  # get occurrences of each term
    return occurrences[term]


def term_frequency_in_index(term_id, document_id, index):
    """
    Occurrences of a term in the document using the inverted index
    """
    posting_list = []
    try:
        posting_list = index[term_id]
    except KeyError:
        print('no')
    for doc in posting_list:
        if doc[0] == str(document_id):  # make it directly int
            return doc[1]
    return 0


def document_frequency(term_id, index):
    """
    Number of documents in which the term appears
    """
    posting_list = index[term_id]
    return len(posting_list)
