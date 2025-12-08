list = [23,54,87,23,87,123,7,68,54,8,90,12,34,56,78]
n= len(list)
for i in range (1,n):
    insertIndex = i
    currentValue = list.pop(i)
    for j in range (i-1,-1,-1):
        if list[j]> currentValue:
            insertIndex=j
    list.insert(insertIndex,currentValue)
    # print(list) #for understanding the process step by step
    
print(list)
    