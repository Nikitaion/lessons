def LineAnalysis(line):
    result = True
    pattern = ''

    symbolNum = 1
    while True:
        try:
            if line[symbolNum] == '*':
                break
            pattern += line[symbolNum]
            symbolNum += 1
        except:
            result = False
            break
    lineForCompare = '*'
    while len(lineForCompare) < len(line):
        lineForCompare += pattern
        lineForCompare += '*'

    if lineForCompare != line:
        result = False

    return result