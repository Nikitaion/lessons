def TheRabbitsFoot(s, encode):
    #s - string
    #encode - bool value. If True - need encode. If False - need decode
    result = ''

    if encode:
        withoutSpases = s.replace(' ', '')
        sqrt = pow(len(withoutSpases), 0.5)

        line = int(sqrt)
        column = round(sqrt)

        if (line * column < len(withoutSpases)):
            line += 1

        letterList = [[''] * column for i in range(line)]

        count = 0
        y = 0
        #massive[line][column]
        #in for cicle add letter to manylinemassive by withoutSpases[x]

        #to DO: if ''
        for x in withoutSpases:
            letterList[count][y] = x
            y += 1
            if (y == column):
                y = 0
                count += 1
                
        #Here we aleady make list with ''
        #if (letterList[x][y] == ''): continue

        for x in range(0, column):
            for y in range(0, line):
                result += letterList[y][x]
            result += ' '

    else:
        line = 1
        column = 0
        for x in s:
            if (x == ' '):
                break
            column +=1

        for x in s:
            if (x == ' '):
                line +=1
        
        letterList = [[''] * column for i in range(line)]
        withoutSpases = s.replace(' ', '')

        x = 0
        y = 0
        splitted = s.split()
        for word in splitted:
            for letter in word:
                letterList[x][y] = letter
                y += 1
            y = 0
            x += 1

        x = 0
        y = 0
        for bukva in range(len(withoutSpases)):
            result += letterList[x][y]
            x += 1
            if len(letterList) == x:
                x = 0
                y += 1

    return result