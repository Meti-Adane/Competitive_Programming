class Solution:
    def relativeSortArray(self, arr1, arr2):
        arr1.sort()
        sorted_array = []
        remaining_numbers = []
        for i in arr2:
            for j in range (arr1.count(i)):
                sorted_array.append(i)
        if arr1 not in arr2:
            k = 0
            while k < len(arr1):
                if arr1[k] not in sorted_array:
                    remaining_numbers.append(arr1[k])
                k +=1
            sorted_array += remaining_numbers
        return sorted_array