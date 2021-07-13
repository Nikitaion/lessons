def Keymaker(k):
    doors = ['1' for i in range(k)]
    for i in range(k):
        for j in range(i+1, k, i+2):
            if int(doors[j]):
                doors[j] = '0'
            else:
                doors[j] = '1'
    return ''.join(doors)

# https://skillsmart.ru/algo/lvl1/oo0b.html