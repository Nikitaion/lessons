def odometer(oksana):
    kmh = 0
    sum = 0
    lastHour = 0
    for index, value in enumerate(oksana):
        if (index % 2 == 0):
            kmh = value
        else:
            sum = sum + kmh * (value - lastHour)
            lastHour = value

    return sum

x = odometer([0,1,15,2,0,6,25,7,30,8,10,10,0,13]) 
print(x)
print(15+25+30+20)