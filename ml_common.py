class MLFeatureAnalyzer(object):
    def __init__(self, data: list):
        self.data = data

    def analyze(self) -> list:
        results = []
        for row in self.data:
            results.append(self.analyze_row(row))

        return results

    def analyze_row(self, row) -> dict:
        pass


class TXTFileFeeder(object):
    def __init__(self, data_file_path):
        data = open(data_file_path, 'r').read()
        self.lines = self.filter_lines(data.split("\n"))

    # noinspection PyMethodMayBeStatic
    def filter_lines(self, lines):

        filtered_line_list = []

        for line in lines:
            if line != '':
                filtered_line_list.append(line.strip())

        return filtered_line_list