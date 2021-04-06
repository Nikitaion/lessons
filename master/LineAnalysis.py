def LineAnalysis(line):
    result = False
    pattern = ''

    symbolNum = 1
    while True:
        try:
            if line[symbolNum] == '*':
                break
            pattern += line[symbolNum]
            symbolNum += 1
        except:
            break
    lineForCompare = '*'
    while len(lineForCompare) < len(line):
        lineForCompare += pattern
        lineForCompare += '*'

    if lineForCompare == line:
        result = True

    return result