def odometer(oksana):
    kmh = 0
    sum = 0
    lastHour = 0
    for num in oksana:
        if (oksana.index(num) % 2 == 0):
            kmh = num
        else:
            sum = sum + kmh * (num - lastHour)
            lastHour = num
    return sum