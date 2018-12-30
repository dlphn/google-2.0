import os
import indexBuilder


class CS276Index:

    def __init__(self):
        self.index = None

    def build(self, half=False):
        data = ""
        for file_id in range(10):
            for filename in os.listdir("pa1-data/" + str(file_id)):
                with open("pa1-data/" + str(file_id) + "/" + filename) as f:
                    read_data = f.read()
                    data = data + read_data
        if half:
            data = data[:len(data)//2]
        self.index = indexBuilder.IndexBuilder('CS276', data)
        self.index.build()
        self.index.get_size()

    def get_tokens(self):
        print(self.index.get_tokens())

    def get_vocabulary(self):
        print(self.index.get_vocabulary())


if __name__ == "__main__":
    index = CS276Index()
    index.build(half=True)
    # index.get_tokens()
    # index.get_vocabulary()

    print("For half of the text:")
    index.build(half=True)






