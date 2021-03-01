def UFO(N, data, octal):
    result = []
    if octal:
        for num in data:
            result.append(int(str(num), base=8))
    else:
        for num in data:
            result.append(int(str(num), base=16))

    return result

