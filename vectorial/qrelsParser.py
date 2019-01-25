class QrelsParser:
    def __init__(self):
        pass

    def parse_all(self, data):
        dict = {}
        lines = data.split('\n')
        for line in lines:
            if line != '':
                rel = line.split()
                dict.setdefault(int(rel[0]), []).append(int(rel[1]))
        return dict


if __name__ == "__main__":
    parser = QrelsParser()
    with open("../CACM/qrels.text") as f:
        read_data = f.read()

    dic = parser.parse_all(read_data)
    print(dic)

