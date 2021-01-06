
def selection_sort(l1):
    for i in range (len(l1)):
        curr = i
        for j in range (i+1, len(l1)):
            if l1[i] > l1[j]:
                curr = j
        l1[curr], l1[i] = l1[i], l1[curr]

    return l1
l1 = [3, 4, 20, 12, 0, 4]
print(selection_sort(l1))



