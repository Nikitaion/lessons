def WordSearch(len, s, subs):
    sequenceOfLines = []
    result = []
    PlacesInALine = len
    # len - alignment width
    # s - string
    # subs - target word

    sequenceOfLines.append('')

    splitted = s.split()
    for item in splitted:
        itemLen = 0
        for c in item:
            itemLen += 1
        
        #Сперва смотрим может ли слово зайти в эту строчку. 
        #Если да - запускаем,
        while True:
            if itemLen <= PlacesInALine:
                lastElement = sequenceOfLines.pop()
                if lastElement == '':
                    sequenceOfLines.append(item)
                else:
                    sequenceOfLines.append(lastElement + ' ' + item)
                PlacesInALine -= itemLen
                PlacesInALine -= 1 #и ещё минус пробел
                break
            else:
                #если нет и строчка уже частично заполнена - создаём следующую строчку.
                if PlacesInALine != len:
                    sequenceOfLines.append('')
                    PlacesInALine = len
                    #Тут не выполняется break и цикл начнется заново. Он проверит вмещается ли теперь слово в строку, если нет - пойдет в местный else
                else:
                    startValue = 0
                    endValue = len
                    needToAdd = True
                    sequenceOfLines.pop()

                    while needToAdd:
                        sequenceOfLines.append(item[startValue:endValue])
                        #Тут проверка на то, закончилось ли слово
                        if endValue >= itemLen:
                            needToAdd = False
                        startValue = endValue
                        endValue +=len
                    sequenceOfLines.append('')
                    break
                    #Сюда попадает если в строке ничего не записано и при этом места на слово не хватает. 

    lastElement = sequenceOfLines.pop()
    if lastElement != '':
        sequenceOfLines.append(lastElement)

    for item in sequenceOfLines:
        found = item.find(subs)
        if found == -1:
            result.append(0)
        else:
            #Тут found == индексу вхождения первой буквы
            itemLen = 0
            subsLen = 0
            for c in item:
                itemLen += 1
            for c in subs:
                subsLen += 1

            startValue = 0
            while True:
                found = item.find(subs, startValue)

                if found == 0 and found + subsLen == itemLen or found == 0 and item[found + subsLen] == ' ' or item[found - 1] == ' ' and found + subsLen == itemLen:
                    result.append(1)
                    break
                
                if startValue >= itemLen:
                    result.append(0)
                    break

                if startValue != 0:
                    startValue = startValue + subsLen
                else:
                    startValue = found + subsLen

    return result