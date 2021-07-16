import sys
from os import path
from pandas import read_csv


class ColorRecognizer:
    def __init__(self):
        self.colorCsv = read_csv(path.join(path.dirname(
            __file__),  'colors.csv'))

    def getColorName(self, rgbCode):
        R, G, B, _ = rgbCode
        minimum = 10000
        for i in range(0, len(self.colorCsv)):
            csvRow = self.colorCsv.loc[i]

            d = abs(R - int(csvRow['R'])) + abs(G -
                                                int(csvRow['G'])) + abs(B - int(csvRow['B']))
            if(d <= minimum):
                minimum = d
                cname = csvRow["color_name"]
        return cname


def main(args):
    pass


if __name__ == '__main__':
    sys.exit(main(sys.argv))
