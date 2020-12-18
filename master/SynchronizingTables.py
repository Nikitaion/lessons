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
                if (addToList == True):
                    newSalaryList.append(value)
                    addToList = False
                    continue
                if (value == idsValue):
                    addToList = True
                    continue

    return newSalaryList