def MisterRobot(N, data):
    result = [False,True]
    i = 0
    per = 2
    while per == 2:
        per = 1
        for i in range(N-1):
            if data[i] > data[i+1] and i < N-2:
                data[i],data[i+1],data[i+2] = data[i+1],data[i+2],data[i]
                per = 2    
                break
            if data[i] > data[i+1]:
                per = 0
        if per == 1 or per == 0: return result[per]

MisterRobot(7, [1,3,4,5,6,2,7])