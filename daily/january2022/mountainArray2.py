class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        i = 0
        while i < len(arr)-1 and arr[i] < arr[i+1]:
            i += 1
        if i == 0 or i == len(arr)-1:
            return False
        i += 1
        while i < len(arr):
            if arr[i] >= arr[i-1]:
                return False
            i += 1
        return True
        