def WordSearch(len, s, subs):
    sequenceOfLines = []
    result = []
    #Сделать переменную, в которой написано сколько в строчке осталось места(прибавлять ещё пробел)
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
                    #И надо теперь проверить может ли слово вместиться в пустую строку
                #Если строка пустая - значит нужно записать в неё часть слова на кол-во доступных символов в строчке(while?), 
                else:
                    startValue = 0
                    endValue = len
                    
                    needToAdd = True
                    sequenceOfLines.pop() #Удаляем последнюю пустую запись. Проверить всегла ли последняя запись пустая
                    while needToAdd:
                        sequenceOfLines.append(item[startValue:endValue]) #string[start:end]: извлекается последовательность символов начиная с индекса start по индекс end
                        #Выше нужно не  0 и лен, а переменные, которые будут увеличиваться с каждым while. 
                        #Например start и end. На следующий while будет start += 1, а end +=len вроде, надо проверить. Скорее всего нет, возможно +=len превысит слово
                        #Тут проверка на то, закончилось ли слово
                        if endValue >= itemLen: #Проверить нужно ли равно
                            needToAdd = False
                        startValue = endValue
                        endValue +=len
                    sequenceOfLines.append('')
                    break
                    #Сюда попадает если в строке ничего не записано и при этом места на слово не хватает. 
                    #Нужно дописать часть слова по длине строки и учесть, что продолжение слова может уйти ещё на множество строк (while?)
                    #Если в строчке недостаточно места на слово - нужно написать  в неё только часть этого слова

    lastElement = sequenceOfLines.pop()
    if lastElement != '':
        sequenceOfLines.append(lastElement)

    
    #Тут нужно реализовать поиск в каждой строке на целевое слово


    for item in sequenceOfLines:
        found = item.find(subs)
        if found == -1:
            result.append(0)
        else:
            #Можно тут в случае вхождения начинать искать это вхождение и проверять на наличие пробелов или конца строки
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



#Функция len() возвращает длину строки.
#len('The first president of the organization..') #=> 41


#Как разделить строку по заданному символу?
#Здесь нам поможет метод split(), который разбивает строку по заданному символу или по нескольким символам.
#'This is great'.split(' ')
##=> ['This', 'is', 'great']
#'not--so--great'.split('--')
##=> ['not', 'so', 'great']
#Ещё есть интересный метод — rsplit(разбивает строку справа налево). Буквально на днях понадобилось мне разбить строки вида «1:2:3:4:5:data» по последнему разделителю. Сначала пробовал так «str.split(':',-1)» — не получилось. Погуглил — нашел rsplit. Да, это есть в офф. документации. Но в процессе гугления понял, что много народа об этом не знают.



#Метод splitlines() разделяет строки по символам разрыва строки.
#sentence = "It was a stormy night\nThe house creeked\nThe wind blew."
#sentence.splitlines()
##=> ['It was a stormy night', 'The house creeked', 'The wind blew.']
#(Возможно можно будет добавить /n каждые len симвоволов или до пробелов и потом разделить


#Как удалить пробелы из начала строки (из её левой части), из её конца (из правой части), или с обеих сторон строки?
#Здесь нам пригодятся, соответственно, методы lstrip(), rstrip() и strip().
#string = '  string of whitespace    '
#string.lstrip() #=> 'string of whitespace    '
#string.rstrip() #=> '  string of whitespace'
#string.strip() #=> 'string of whitespace'


#Метод partition() разбивает строку по заданной подстроке. После этого результат возвращается в виде кортежа. При этом подстрока, по которой осуществлялась разбивка, тоже входит в кортеж.
#sentence = "If you want to be a ninja"
#print(sentence.partition(' want '))
##=> ('If you', ' want ', 'to be a ninja')


#S.ljust(width, fillchar=" ")	
#Делает длину строки не меньшей width, по необходимости заполняя последние символы символом fillchar


#lstrip(): удаляет начальные пробелы из muka2010строки
#rstrip(): удаляет конечные пробелы из строки
#strip(): удаляет начальные и конечные пробелы из строки
#ljust(width): если длина строки меньше параметра width, то справа от строки добавляются пробелы, чтобы дополнить значение width, а сама строка выравнивается по левому краю

#split([delimeter[, num]]): разбивает строку на подстроки в зависимости от разделителя
#join(strs): объединяет строки в одну строку, вставляя между ними определенный разделитель


#Каждая строка проверяется на наличие в ней заданного целого слова (ограниченного либо пробелами, либо началом/концом строки).




#Возможно нужно смотреть на то, что должны быть по соседству пробелы или конец/начало строки
print(WordSearch(12, 'строка разбивается на набор строк через выравнивание по заданной ширине.', 'строк'))

print(WordSearch(1, '0 1 2 3 4 5 6 7 8 9', '3'))

print(WordSearch(1, '0 1 2 3 4 5 6 7 8 9', '3'))
print(WordSearch(3, '0 1 2 3 4 5 6 7 8 9', '3'))
print(WordSearch(5, '0 1 2 3 4 5 6 7 8 9', '3'))
print(WordSearch(8, '0 1 2 3 4 5 6 7 8 9', '3'))


print(WordSearch(7, 'что то привето какддела', 'то'))
print(WordSearch(7, 'что то привето какддела', 'то'))
print(WordSearch(7, 'что то привето какддела', 'то'))
print(WordSearch(7, 'что то привето какддела', 'то'))
print(WordSearch(7, 'что то привето какддела', 'то'))


print(WordSearch(5, 'если длина строки меньше параметра width, то справа от строки добавляются пробелы, чтобы дополнить значение width, а сама строка выравнивается по левому краю', 'то'))
print()


sequenceOfLines = []
#У нас есть пустой список
sequenceOfLines.append('')

itemLen = 10
word = '1234567890'
#Пусть нужно вписывать по 3 символа

len = 2
startValue = 0
endValue = len

needToAdd = True
sequenceOfLines.pop() #Удаляем последнюю пустую запись
while needToAdd:
    sequenceOfLines.append(word[startValue:endValue]) #string[start:end]: извлекается последовательность символов начиная с индекса start по индекс end
    #Выше нужно не  0 и лен, а переменные, которые будут увеличиваться с каждым while. 
    #Например start и end. На следующий while будет start += 1, а end +=len вроде, надо проверить. Скорее всего нет, возможно +=len превысит слово
    #Тут проверка на то, закончилось ли слово
    if endValue >= itemLen: #Проверить нужно ли равно
        needToAdd = False
    startValue = endValue
    endValue +=len



lastElement = sequenceOfLines.pop()
if lastElement == '':
    sequenceOfLines.append('hehehe')
else:
    sequenceOfLines.append(lastElement + ' ' + 'hehehe')
x = sequenceOfLines[-1]





WordSearch(3, 'qwerty wer ert rty', '2')

z = '1sagas 2asgasgas 3asgasgas 4asgasgas 5gdsgsdgs 6fhethreh 7grhghfdhd'
x = 'This is great'.split(' ')
print(x)
print(x[0])
print(x[1])
print(x[2])

c = z.split(' ', 3)
print(c)

text = "Это был огромный, в два обхвата дуб, с обломанными ветвями и с обломанной корой"
# разделение по пробелам
splitted_text = text.split()
print(splitted_text)
print(splitted_text[6])     # дуб,
 
# разбиение по запятым
splitted_text = text.split(",")
print(splitted_text)
print(splitted_text[1])     # в два обхвата дуб
 

#Можно следующее проверить не только по пробелам, но и по любым символам
# разбиение по первым пяти пробелам
splitted_text = text.split(" ", 5)
print(splitted_text)        
print(splitted_text[5])     # обхвата дуб, с обломанными ветвями и с обломанной корой










#Вариант - засплитить весь текст
#Перед тем как взять 2 слова нужно проверить текущее слово на кол-во символов и если больше 16 - разделить его. Посмотреть на разделенное слово и разделить если нужно.
#Потом взять первые 2 слова и если вместе + пробел меньше 16 символов, то объединить и проверить с 3 словом + пробел и.т.д. пока не будет с лишним словом больше 16 символов
#Потом брать следующее слово или последнее использованное, но не прошедшее
#Вставлять получившиеся строчки в новый лист
