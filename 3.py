def potega(list1, list2):
    list3 = []
    if len(list1) == len(list2):
        for x in range(len(list1)):
            list3.append(list1[x] ** list2[x])

    return list3

list1 = [2, 2, 2]
list2 = [0, 1, 2]

print(potega(list1, list2))