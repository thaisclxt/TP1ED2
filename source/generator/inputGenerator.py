def convertToStr(*args):
    data = []
    for group in args:
        for element in group:
            data.append(str(element))
            data.append(" ")
        data.pop()
        data.append("\n")

    return "".join(data)

def txt(file, data):
    file.write(data)
    file.close

import geradorDMN as dmn
import geradorS as s
import sys

group = dmn.Group(sys.argv)

innerGroup = s.innerGroup(group.generatedNumbers)

group.shuffleNumber()
txt(open("input.txt", "w+"), convertToStr(group.generatedNumbers))

underAverageGroup = s.underAverageGroup(group.generatedNumbers, group.media)
overAverageGroup = s.overAverageGroup(group.generatedNumbers, group.media)
txt(open("search.txt", "w+"), convertToStr(underAverageGroup, overAverageGroup, innerGroup))