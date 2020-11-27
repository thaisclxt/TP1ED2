def innerGroup(generatedNumbers):
    innerGroup = []
    for i in range(25):
        innerGroup.append(generatedNumbers[i])

    for i in range(10000 - 25, 10000):
        innerGroup.append(generatedNumbers[i])
    return innerGroup

def underAverageGroup(generatedNumbers, media):
    underAverageGroup = []
    cont = 0
    for x in generatedNumbers:
        if x <= media and cont < 50:
            underAverageGroup.append(x)
            cont += 1
    return underAverageGroup

def overAverageGroup(generatedNumbers, media):
    overAverageGroup = []
    cont = 0
    for x in generatedNumbers:
        if x >= media and cont < 50:
            overAverageGroup.append(x)
            cont += 1
    return overAverageGroup