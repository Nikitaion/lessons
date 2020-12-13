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