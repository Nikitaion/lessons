def ConquestCampaign(N, M, L, battalion):
    day = 1
    notAllFieldColoured = True

    if(N == 1 and M == 1):
        return day

    battleground = []
    for i in range(1, N+1):
        newList = [0] * M
        battleground.append(newList)

    for index, value in enumerate(battalion):
        battalion[index] = value - 1

    even = True
    X = 0
    Y = 0
    for index, value in enumerate(battalion):
        if even:
            X = value
            even = False
            continue
        else:
            Y = value
            even = True
        battleground[X][Y] = 1
    
    listForNextPaint = []
    while notAllFieldColoured:
        for indexFullList, valueFullList in enumerate(battleground):
            for indexSubList, valueSubList in enumerate(valueFullList):
                if (valueSubList == 1):
                    if (0 <= indexFullList - 1 < N):
                        if(battleground[indexFullList - 1][indexSubList] == 0):
                            listForNextPaint.append([indexFullList - 1, indexSubList])
                    if (0 <= indexFullList + 1 < N):
                        if(battleground[indexFullList + 1][indexSubList] == 0):
                            listForNextPaint.append([indexFullList + 1, indexSubList])
                    if (0 <= indexSubList - 1 < M):
                        if(battleground[indexFullList][indexSubList - 1] == 0):
                            listForNextPaint.append([indexFullList, indexSubList - 1])
                    if (0 <= indexSubList + 1 < M):
                        if(battleground[indexFullList][indexSubList + 1] == 0):
                            listForNextPaint.append([indexFullList, indexSubList + 1])
        

        for indexForNextPaint, valueForNextPaint in enumerate(listForNextPaint):
            for indexSubList, valueSubList in enumerate(valueForNextPaint):
                if even:
                    X = valueSubList
                    even = False
                    continue
                else:
                    Y = valueSubList
                    even = True

                battleground[X][Y] = 1

        listForNextPaint.clear()

        notAllFieldColoured = False

        for indexFullList, valueFullList in enumerate(battleground):
            for indexSubList, valueSubList in enumerate(valueFullList):
                if (valueSubList == 0):
                    notAllFieldColoured = True
                    break

        day += 1

    return day