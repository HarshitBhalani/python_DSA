list = [23,54,87,23,87,123,7,68,54,8,90,12,34,56,78]

n= len(list)

for i in range (n-1):
    minIndex = i
    for j in range (i+1,n):
        if list[j]< list[minIndex]:
            minIndex = j
    minValue = list.pop(minIndex)
    list.insert(i, minValue)
    # print(list) #for understanding the process step by step
print(list)
