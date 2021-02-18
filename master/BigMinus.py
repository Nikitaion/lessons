def BigMinus(s1, s2):
    x = int(s1) - int(s2)
    if x < 0:
        x *= -1

    return str(x)