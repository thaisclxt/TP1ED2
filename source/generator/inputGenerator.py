def convertToStr(*group):
    data = []
    for g in group:
        data += [str(x) + " " for x in g]
        data += "\n"
        
    return "".join(data)

def txt(file, data):
    file.write(data)
    file.close

import geradorDMN as dmn
import geradorS as s
import sys

g = dmn.Group(sys.argv)

innerGroup = s.innerGroup(g.group)

g.shuffleNumber()
txt(open("input.txt", "w+"), convertToStr(g.group))

underAverageGroup = s.underAverageGroup(g.group, g.media)
overAverageGroup = s.overAverageGroup(g.group, g.media)
txt(open("search.txt", "w+"), convertToStr(underAverageGroup, overAverageGroup, innerGroup))