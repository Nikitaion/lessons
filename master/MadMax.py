def Telesort(N, Tele):
    Tele.sort()
    
    middlePoint = int((N - 1) / 2 + 1)

    firstParOfList = Tele[:middlePoint - 1]
    secondParOfList = Tele[middlePoint - 1:]
    secondParOfList.reverse()

    impulse = firstParOfList + secondParOfList

    return impulse
