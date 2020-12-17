def SynchronizingTables(N, ids, salary):    
    sortedIds = ids.copy()
    sortedIds.sort()

    sortedSalary = salary.copy()
    sortedSalary.sort()

    salaryWithIds = [(x,y) for x,y in zip(sortedIds,sortedSalary)]
    addToList = False
    newSalaryList = []

    for idsIndex, idsValue in enumerate(ids):
        for salaryIndex, salaryValue in enumerate(salaryWithIds):
            addToList = False
            for index, value in enumerate(salaryValue):
                if (value == idsValue):
                    if value == 67:
                        print("wtf")
                    addToList = True
                    continue

                if (addToList == True):
                    if value == 67:
                        print("wtf")
                    newSalaryList.append(value)
                    addToList = False
                    
    return newSalaryList