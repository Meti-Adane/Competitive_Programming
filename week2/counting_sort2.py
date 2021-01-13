import random
def counting_sort2(l1):
    size = max(l1) if max(l1) > abs(min(l1)) else abs(min(l1))
    mid = ((size) * 2) // 2
    negative_array = [0 for i in range(size + 1)]
    positive_array = [0 for i in range(size + 1)]
    sorted_list = []

    for i in l1:
        if i < 0:
            negative_array[i * -1] += 1
        else:
            positive_array[i] += 1

    leftSide = mid
    while leftSide >= 0:
        if negative_array[leftSide] > 0:
            sorted_list.extend(leftSide * -1 for i in range(negative_array[leftSide]))
        leftSide -= 1

    rightSide = 0
    while rightSide <= mid:
        curr = positive_array[rightSide]
        if curr > 0:
            sorted_list.extend(rightSide for i in range(positive_array[rightSide]))
        rightSide += 1

    return sorted_list


def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr
l2 = [random.randint(-50, 100) for j in range(100)]
print(mergeSort(l2))