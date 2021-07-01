# https://skillsmart.ru/algo/lvl1/oafd.html

def Football(F, N):
    k = 0
    if F == sorted(F):
        return False
    for i in range(N-1):
        for j in range(k, N):
            f = F[:]
            if i != j:
                f[i], f[j] = f[j], f[i]
            if f == sorted(F) or f[::-1] == sorted(F):
                return True
        k += 1
    return False