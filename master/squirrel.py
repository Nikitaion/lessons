def squirrel(N):
    factorial = 1

    if (N >= 0):
        for i in range(1, N + 1):
            factorial = factorial*i
        return int(str(factorial)[0])
    else:
       return 0