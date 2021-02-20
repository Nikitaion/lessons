def BigMinus(s1, s2):
    bigger = s1
    smaller = s1

    result = ''

    if len(s1) > len(s2):
        bigger = s1
    elif len(s1) < len(s2):
        bigger = s2
    else:
        count = 0
        for letter in s1:
            if int(letter) > int(s2[count]):
                bigger = s1
                break
            elif int(letter) < int(s2[count]):
                bigger = s2
                break
            else:
                count += 1

    if bigger == s1:
        smaller = s2

    count = 1
    while count < len(bigger) + 1:
        
        biggerNum = int(bigger[len(bigger) - count])
        if len(smaller) - count >= 0:
            smallerNum = int(smaller[len(smaller) - count])
        else:
            smallerNum = 0
        if biggerNum >= smallerNum:
            result += str(biggerNum - smallerNum)
        else:
            #borrowNum = int(bigger[len(bigger) - count - 1]) #Если нужно будет занять у предудущего числа
            #if borrowNum > 0:
            #    borrowNum -= 1
            #
            #    list1 = list(bigger)
            #    list1[len(bigger) - count - 1] = str(borrowNum)
            #    bigger = ''.join(list1)
            #    biggerNum += 10
            #    result += str(biggerNum - smallerNum)
            #else:
            anotherCount = count
            borrowNum = int(bigger[len(bigger) - anotherCount - 1])
            if borrowNum == 0:
                while borrowNum == 0:
                    anotherCount += 1
                    borrowNum = int(bigger[len(bigger) - anotherCount - 1])

                borrowNum -= 1
                list1 = list(bigger)
                list1[len(bigger) - anotherCount - 1] = str(borrowNum)
                bigger = ''.join(list1)

                while anotherCount != count - 1:
                    anotherCount -= 1
                    list1 = list(bigger)
                    list1[len(bigger) - anotherCount - 1] = str(int(bigger[len(bigger) - anotherCount - 1]) + 9)
                    if anotherCount == count - 1:
                        biggerNum = list1[len(bigger) - anotherCount - 1]
                        biggerNum = int(biggerNum)
                    else:
                        bigger = ''.join(list1)

            result += str(biggerNum + 1 - smallerNum)




        count += 1
    result = int(result[::-1]) #reverse and to int result
    return str(result)