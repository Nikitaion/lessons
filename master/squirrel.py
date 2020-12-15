def ConquestCampaign(N, M, L, battalion):

    day = 1
    notAllFieldColoured = True

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
    


    ##########################################

    for indexN, valueN in enumerate(battleground):
        for indexM, valueM in enumerate(valueN):
            #print(index1)
            print(valueM, end="\t")
        print("\n")

    #########################################
    listForNextPaint = []
    
    while notAllFieldColoured:
        for indexFullList, valueFullList in enumerate(battleground):
            for indexSubList, valueSubList in enumerate(valueFullList):
                if (valueSubList == 1):
                    if (0 <= indexFullList - 1 < len(valueFullList)):
                        listForNextPaint.append([indexFullList - 1, indexSubList])
                    if (0 <= indexFullList + 1 < len(valueFullList)):
                        listForNextPaint.append([indexFullList + 1, indexSubList])
                    if (0 <= indexSubList - 1 < len(valueFullList)):
                        listForNextPaint.append([indexFullList, indexSubList - 1])
                    if (0 <= indexSubList + 1 < len(valueFullList)):
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
                #battleground[indexForNextPaint][indexSubList] = 1

        listForNextPaint.clear()

        #checkForAllFieldColored()

        notAllFieldColoured = False

        for indexFullList, valueFullList in enumerate(battleground):
            for indexSubList, valueSubList in enumerate(valueFullList):
                if (valueSubList == 0):
                    notAllFieldColoured = True
                    #--?
                    break
            



        print("")


        for indexN, valueN in enumerate(battleground):
            for indexM, valueM in enumerate(valueN):
            #print(index1)
                print(valueM, end="\t")
            print("\n")




        day += 1


    return day

def PaintTheFields(listOfFields):
    even = True
    X = 0
    Y = 0
    for index, value in enumerate(listOfFields):
        if even:
            X = value
            even = False
            continue
        else:
            Y = value
            even = True

        battleground[X - 1][Y - 1] = 1




    


def MakeListOfList(N, M):
    battleground = []
    for i in range(1, N+1):
        newList = [0] * M
        battleground.append(newList)

    for indexN, valueN in enumerate(battleground):
        for indexM, valueM in enumerate(valueN):
            #print(index1)
            print(valueM, end="\t")
        print("\n")
    return battleground

def PaintTheFields(listOfFields):
    even = True
    X = 0
    Y = 0
    for index, value in enumerate(listOfFields):
        if even:
            X = value
            even = False
            continue
        else:
            Y = value
            even = True

        battleground[X - 1][Y - 1] = 1

def PaintNeighboringFields(battleground):
    listForNextPaint = []
    
    while notAllFieldColoured:
        for indexFullList, valueFullList in enumerate(battleground):
            for indexSubList, valueSubList in enumerate(valueFullList):
                if (valueSubList == 1):
                    if (0 <= indexFullList - 1 < len(valueFullList)):
                        listForNextPaint.append([indexFullList - 1], [indexSubList])
                    if (0 <= indexFullList + 1 < len(valueFullList)):
                        listForNextPaint.append([indexFullList + 1], [indexSubList])
                    if (0 <= indexSubList - 1 < len(valueFullList)):
                        listForNextPaint.append([indexFullList], [indexSubList - 1])
                    if (0 <= indexSubList + 1 < len(valueFullList)):
                        listForNextPaint.append([indexFullList], [indexSubList + 1])
        

        for indexForNextPaint, valueForNextPaint in enumerate(listForNextPaint):
            for indexSubList, valueSubList in enumerate(valueForNextPaint):
                battleground[indexForNextPaint, indexSubList] = 1

        listForNextPaint.clear()

        checkForAllFieldColored()

        notAllFieldColoured = False

        for indexFullList, valueFullList in enumerate(battleground):
            for indexSubList, valueSubList in enumerate(valueFullList):
                if (valueSubList == 0):
                    notAllFieldColoured = True #Если находит хоть одтн не закрашенный - продолжаем
                    #Нужно ли минус один делать подумать
        
        day += day
            #paintNeighboringFields. And at the same time, you do not need to then detect a new shaded field and mark it
            #Therefore, we just remember the nearest cells that do not go beyond the boundaries of the array.




#k = MakeListOfList(7, 9)
x = ConquestCampaign(9, 9,2, [5,5, 2, 8, 1, 2, 4, 5,6, 7, 8, 8, 0,9 , 9,0, 1, 8, 8,1])
