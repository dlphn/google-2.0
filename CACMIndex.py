import CACMParser
import indexBuilder


class CACMIndex:

    def __init__(self):
        self.parser = CACMParser.CACMParser()
        self.index = None

    def build(self):
        with open("CACM/cacm.all") as f:
            read_data = f.read()
        dic = self.parser.parse_documents(read_data)
        data = self.parser.parse_all(dic)
        self.index = indexBuilder.IndexBuilder('CACM', data)
        self.index.build()
        self.index.get_size()

    def get_tokens(self):
        print(self.index.get_tokens())

    def get_vocabulary(self):
        print(self.index.get_vocabulary())


if __name__ == "__main__":
    index = CACMIndex()
    index.build()
    index.get_tokens()
    index.get_vocabulary()
