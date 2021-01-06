def counting_sort(l1):
    occurence_array = [0] * (max(l1) + 1)
    sorted_list = []
    for i in l1:
        occurence_array[i] += 1
    k = 0
    while k < len(occurence_array):
        if occurence_array[k] > 0:
            for i in range (occurence_array[k]):
                sorted_list.append(k)
        k += 1

    return sorted_list


l1 = [3,0, 0, 1, 8, 3, 50, 16, 309, 4, 2, 22, 0, 67]
print(counting_sort(l1))