# question url : https://leetcode.com/contest/weekly-contest-156/problems/unique-number-of-occurrences/

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arrOccurence = dict()
        check = set()

        for i in arr:
            arrOccurence[i] = arr.count(i)
        for keys in arrOccurence.keys():
            check.add(arrOccurence[keys])

        return len(check) == len(arrOccurence)