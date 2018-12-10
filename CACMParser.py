# create function for parse all documents
# create function for getting all document id
# create function for getting .T, .W, .K for each docID


document_seperator = ".I "
title_separator = "\n.T\n"
summary_separator = "\n.W\n"
key_words_separator = "\n.K\n"


class CACMParser:
    def __init__(self):
        pass

    def parse_documents(self, text):
        docs = text.split(document_seperator)[1:]
        dic = {}
        for doc in docs:
            id = doc[:doc.find("\n")]
            dic[id] = doc[doc.find("\n"):]
        return dic

    def get_all_ids(self, text):
        dic = self.parse_documents(text)
        return dic.keys()

    def parse_title(self, dic):
        for id in dic.keys():
            doc = dic[id]
            title = None
            if len(doc.split(title_separator)) == 2:
                title = doc.split(title_separator)[1].split("\n")[0]
            dic[id] = title
        return dic

    def parse_summary(self, dic):
        for id in dic.keys():
            doc = dic[id]
            summary = None
            if len(doc.split(summary_separator)) == 2:
                summary = doc.split(summary_separator)[1].split(".B")[0]
            dic[id] = summary
        return dic

    def parse_key_words(self, dic):
        for id in dic.keys():
            doc = dic[id]
            key_words = None
            if len(doc.split(key_words_separator)) == 2:
                key_words = doc.split(key_words_separator)[1].split(".C")[0]
            dic[id] = key_words
        return dic


parser = CACMParser()
with open("CACM/cacm.all") as f:
    read_data = f.read()

dic = parser.parse_documents(read_data)
print(dic.keys())

# print(parser.parse_title(dic))
# print(parser.parse_summary(dic))
# print(parser.parse_key_words(dic))

