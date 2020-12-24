def PatternUnlock(N, hits):
    result = 0

    currentNumber = -1
    previousNumber = -1

    layout = []
    for i in range(0, 3):
        newList = [6 - i, 1 + i, 9 - i]
        layout.append(newList)

    for number in hits:
        currentNumber = number
        if previousNumber == -1:
            previousNumber = number
            continue

        for indexFullList, valueFullList in enumerate(layout):
            for indexSubList, valueSubList in enumerate(valueFullList):
                if (valueSubList == previousNumber):
                    indexXx = indexFullList
                    indexXy = indexSubList
                if (valueSubList == currentNumber):
                    indexYx = indexFullList
                    indexYy = indexSubList

        if(indexXx == indexYx + 1 and indexXy == indexYy + 1 or 
           indexXx == indexYx - 1 and indexXy == indexYy - 1 or 
           indexXx == indexYx - 1 and indexXy == indexYy + 1 or 
           indexXx == indexYx + 1 and indexXy == indexYy - 1):
            result += 1.4142135623730951
        else:
            result += 1

    result = round(result, 5)

    result = float(str(result).replace('0',''))
    result = int(str(result).replace('.',''))
    result = int(str(result).replace('0',''))

    return result