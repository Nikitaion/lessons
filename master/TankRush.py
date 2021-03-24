def TankRush(H1, W1, S1, H2, W2, S2):
    
    def find(S1, St_start, St_end, Col_start, Col_end):
        S1_new = S1[St_start:St_end]
        for i1 in range(len(S1_new)):
            S1_new[i1] = S1_new[i1][Col_start:Col_end]
        return S1_new

    # Разбиваем строки на подстроки по пробелу
    S1 = S1.split()  
    S2 = S2.split()

    # Ищем подстроку S2[0] во всех строках карты S1
    flag = False
    for i1 in range((H1 - H2) + 1): # строки S1
        index_end = 0
        j1 = 0
        while j1 in range(W1): # столбцы S1
            index_start = S1[i1].find(S2[0], j1)
            if index_start != -1:
                index_end = index_start + W2
                St_end = i1 + H2
                S1_new = find(S1, i1, St_end, index_start, index_end) 
                
                if S1_new == S2:
                    flag = True
                    break
            j1 += 1
            
    return flag