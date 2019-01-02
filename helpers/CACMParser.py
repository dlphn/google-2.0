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
        dic2 = {}
        for id in dic.keys():
            doc = dic[id]
            title = None
            if len(doc.split(title_separator)) == 2:
                title = doc.split(title_separator)[1].split("\n")[0]
            dic2[id] = title
        return dic2

    def parse_summary(self, dic):
        dic2 = {}
        for id in dic.keys():
            doc = dic[id]
            summary = None
            if len(doc.split(summary_separator)) == 2:
                summary = doc.split(summary_separator)[1].split(".B")[0]
            dic2[id] = summary
        return dic2

    def parse_key_words(self, dic):
        dic2 = {}
        for id in dic.keys():
            doc = dic[id]
            key_words = None
            if len(doc.split(key_words_separator)) == 2:
                key_words = doc.split(key_words_separator)[1].split(".C")[0]
            dic2[id] = key_words
        return dic2

    def parse_all(self, dic):
        titles = self.parse_title(dic)
        summaries = self.parse_summary(dic)
        keywords = self.parse_key_words(dic)
        all = {}
        for id in dic.keys():
            all[id] = titles[id]
            if summaries[id] is not None:
                all[id] = all[id] + " " + summaries[id]
            if keywords[id] is not None:
                all[id] = all[id] + " " + keywords[id]
        return all


if __name__ == "__main__":
    parser = CACMParser()
    with open("CACM/cacm.all") as f:
        read_data = f.read()

    dic = parser.parse_documents(read_data)
    # print(dic.keys())
    # print(dic)

    # print(parser.parse_key_words(dic))

    print(parser.parse_all(dic))

    # print(parser.parse_title(dic))
    # print(parser.parse_summary(dic))


