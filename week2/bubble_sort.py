def swap(m, a, b):
    c = m[a]
    m[a] = m[b]
    m[b] = c
    return m
def bubleSort(l1):
    for i in range (len(l1)):
        for j in range (len(l1)):
            if l1[i] < l1[j]:
                swap(l1, i, j)
    return l1

