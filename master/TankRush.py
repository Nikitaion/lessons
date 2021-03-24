def TankRush(H1, W1, S1, H2, W2, S2):
    
    S1 = S1.split()
    S2 = S2.split()

    for i in range(H2):
        flag = False
        for j in range(H1):
            if S2[i] in S1[j]:
                flag = True
                break
            
    return flag

#print(TankRush(3, 4, '343434 234598 023997', 2,2, '34 98'))