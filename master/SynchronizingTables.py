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
            for index, value in enumerate(salaryValue):
                if (addToList == True):
                    newSalaryList.append(value)
                    addToList = False
                    break
                if (value == idsValue):
                    addToList = True

    return newSalaryList