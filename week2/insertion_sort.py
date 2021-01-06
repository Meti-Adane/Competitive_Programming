
def insertionSort(l1):
    for i in range(1, len(l1)):

        curr = l1[i]
        j = i - 1
        while j >= 0 and curr < l1[j]:
            l1[j + 1] = l1[j]
            j -= 1
        l1[j + 1] = curr
    return l1

l = [8, 7, 34, 0, 2, 3]
print(insertionSort(l))