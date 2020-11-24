def innerGroup(group):
    innerGroup = []
    for i in range(25):
        innerGroup.append(group[i])

    for i in range(10000 - 25, 10000):
        innerGroup.append(group[i])
    return innerGroup

def underAverageGroup(group, media):
    underAverageGroup = []
    cont = 0
    for x in group:
        if x <= media and cont < 50:
            underAverageGroup.append(x)
            cont += 1
    return underAverageGroup

def overAverageGroup(group, media):
    overAverageGroup = []
    cont = 0
    for x in group:
        if x >= media and cont < 50:
            overAverageGroup.append(x)
            cont += 1
    return overAverageGroup